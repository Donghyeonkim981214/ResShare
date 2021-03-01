from django.urls import path, include
from . import views

app_name = "shareRes"

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('restaurantDetail/delete',views.restaurantDeleteView.as_view(), name='resDelete'),
    path('restaurantDetail/<str:res_id>',views.restaurantDetailView.as_view(), name='resDetailPage'),
    #path('restaurantDetail/updatePage/update',views.Update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>',views.restaurantUpdateView.as_view(), name='resUpdatePage'),
    path('restaurantCreate/',views.restaurantCreateView.as_view(), name='resCreatePage'),
    #path('restaurantCreate/create',views.Create_restaurant, name='resCreate'),
    path('categoryCreate/',views.categoryCreateView.as_view(), name='cateCreatePage'),
    #path('categoryCreate/create',views.Create_category, name='cateCreate'),
    path('categoryCreate/delete',views.categoryDeleteView.as_view(), name='cateDelete'),
]