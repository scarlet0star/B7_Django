from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductFeed.as_view(), name='product_feed'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
]
