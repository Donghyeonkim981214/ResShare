from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path('reviewCreate/<int:pk>', views.reviewCreateView.as_view(), name='revCreate'),
    path('reviewDelete/<int:pk>', views.reviewDeleteView.as_view(), name='revDelete'),
    path('reviewUpdate/<int:pk>', views.reviewUpdateView.as_view(), name='revUpdate'),
]