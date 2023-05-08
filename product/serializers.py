from rest_framework import serializers
from product.models import Product, ProductCategory


# 상품 피드
class ProductFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "price", "is_free", "image",
                  "place", "category", "views", "transaction_status", "refreshed_at", "is_hide",)
        # "bookmark",


# 상품 등록
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "content", "price", "is_free", "image",
                  "bargain", "place", "refreshed_at",)
        # "category",
