from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import *

from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from . import forms

from . import mixins

from django.contrib.auth.mixins import LoginRequiredMixin

from reviews import models as rev_models

from django.db.models import Avg
# Create your views here.
""" def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants': restaurants}
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html', content) """

class indexView(TemplateView):
    template_name = 'shareRes/index.html'

    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['restaurants'] = Restaurant.objects.all()
        context['title'] = "맛집 공유 사이트"
        return context


""" def restaurantDetail(request,res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant': restaurant}
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html', content) """

class restaurantDetailView(mixins.ReadOnlyModelFormMixin, UpdateView):
    model = Restaurant
    template_name = "shareRes/restaurantDetail.html"
    slug_url_kwarg = "res_id"
    slug_field = "id"
    form_class = forms.RestaurantForm

    def get_context_data(self, **kwargs):
        context = super(restaurantDetailView, self).get_context_data(**kwargs)
        context['title'] = "맛집 소개"
        context['reviews'] = rev_models.Review.objects.filter(restaurant = self.object)
        if self.request.user.is_authenticated:
            try:
                context['user_review'] = rev_models.Review.objects.filter(restaurant = self.object).get(created_by = self.request.user)
            except rev_models.Review.DoesNotExist:
                context['user_review'] = None
        try:
            context['avg_rate'] = rev_models.Review.objects.filter(restaurant = self.object).aggregate(Avg('rate'))
        except rev_models.Review.DoesNotExist:
            context['avg_rate'] = None
        return context

    
""" def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    # return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html', content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category, restaurant_name = name, restaurant_link = link, restaurant_content = content, restaurant_keyword = keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index')) """

class restaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = "shareRes/restaurantCreate.html"
    success_url = reverse_lazy('shareRes:index')
    form_class = forms.RestaurantForm

    def get_context_data(self, **kwargs):
        context = super(restaurantCreateView, self).get_context_data(**kwargs)
        context['title'] = "맛집 추가하기"
        return context


""" def restaurantUpdate(request,res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories': categories, 'restaurant': restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id = change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))"""

class restaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    template_name = "shareRes/restaurantUpdate.html"
    slug_url_kwarg = "res_id"
    slug_field = "id"
    form_class = forms.RestaurantForm

    def get_context_data(self, **kwargs):
        context = super(restaurantUpdateView, self).get_context_data(**kwargs)
        context['title'] = "맛집 수정하기"
        return context


""" def Delete_restaurant(request):
    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index')) """

class restaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy('shareRes:index')
    
    def get_object(self, queryset=None):
      resId = self.request.POST['resId']
      return self.get_queryset().filter(pk=resId).get()


""" def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index')) """

class categoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "shareRes/categoryCreate.html"
    success_url = reverse_lazy('shareRes:cateCreatePage')

    form_class = forms.CategoryForm
    
    def get_context_data(self, **kwargs):
        context = super(categoryCreateView, self).get_context_data(**kwargs)
        context['title'] = "카테고리 추가하기"
        context['categories'] = Category.objects.all()
        return context


""" def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage')) """


class categoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('shareRes:cateCreatePage')

    def get_object(self, queryset=None):
      pk = self.request.POST['categoryId']
      return self.get_queryset().filter(pk=pk).get()
