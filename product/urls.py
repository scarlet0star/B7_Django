from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductFeedView.as_view(), name='product_feed'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),                                              # 상품 등록
    path('<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail_view'),                               # 상품 자세히 보기
    path('category/', views.ProductCategoryView.as_view(), name='product_category_view'),                                   # 카테고리 보기
    path('category/<int:category_id>/', views.ProductCategoryFilterView.as_view(), name='product_category_filter_view'),    # 카테고리별 상품 조회
    path('category/create/', views.ProductCategoryCreateView.as_view(), name='product_category_create_view'),               # 카테고리별 생성
    path('bookmark/', views.ProductBookmarkListView.as_view(), name='product_bookmark_list_view'),                          # 관심상품 리스트 조회
    path('<int:product_id>/bookmark/', views.ProductBookmarkView.as_view(), name='bookmark_view'),                          # 관심상품 등록
]
