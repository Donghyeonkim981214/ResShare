from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from . import forms
from shareRes import models as Res_models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView
from . import models as Rev_models
from django.shortcuts import get_object_or_404

# Create your views here.
class reviewCreateView(LoginRequiredMixin, CreateView):
    template_name = "review/reviewCreate.html"
    form_class = forms.ReviewForm
    model = Rev_models.Review

    def form_valid(self, form):
        review = form.save()
        review.created_by = self.request.user
        review.restaurant = Res_models.Restaurant.objects.get(pk=self.kwargs['pk'])
        review.save()
        return redirect(reverse("shareRes:resDetailPage", kwargs={"res_id": self.kwargs['pk']}))
    
    def get_context_data(self, **kwargs):
        context = super(reviewCreateView, self).get_context_data(**kwargs)
        context['res_id'] = self.kwargs['pk']
        context['title'] = "리뷰 작성"
        return context
    

class reviewDeleteView(DeleteView):
    model = Rev_models.Review

    def get_object(self, queryset=None):
      id = self.request.POST['revId']
      return self.get_queryset().filter(pk=id).get()
    
    def get_success_url(self):
        return reverse("shareRes:resDetailPage", kwargs={"res_id": self.kwargs['pk']})


class reviewUpdateView(UpdateView):
    model = Rev_models.Review
    form_class = forms.ReviewForm
    template_name = "review/reviewUpdate.html"

    def get_object(self, queryset=None):
        review = get_object_or_404(Rev_models.Review, pk=self.kwargs['pk']) #4
        return review

    def get_context_data(self, **kwargs):
        context = super(reviewUpdateView, self).get_context_data(**kwargs)
        context['rev_id'] = self.kwargs['pk']
        context['title'] = "리뷰 수정"
        return context

    def form_valid(self, form):
        review = form.save()
        review.save()
        return redirect(reverse("shareRes:resDetailPage", kwargs={"res_id": self.object.restaurant.id}))
