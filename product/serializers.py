from rest_framework import serializers
from product.models import Product, ProductCategory


"""
"id", "title", "content", "price", "is_free", "image", "bargain", "place", "category",
"views", "transaction_status", "refreshed_at", "is_hide", "created_at", "updated_at", 
"""
# bookmark, user 빠짐


# 상품 피드
class ProductFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # "user", "bookmark",


# 상품 등록
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "content", "price", "is_free", "image",
                  "bargain", "place", "category", "refreshed_at",)
