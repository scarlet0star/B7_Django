from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductFeedView.as_view(), name='product_feed'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail_view'),
    path('category/', views.ProductCategoryView.as_view(), name='product_category_view'),
    path('bookmark/', views.ProductBookmarkView.as_view(), name='product_bookmark_view'),
]
