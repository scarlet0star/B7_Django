from rest_framework import serializers
from product.models import Product, ProductCategory


"""
"id": "아이디",
"user": "유저아이디",
"title": "제목",
"content": "내용",
"price": "가격",
"is_free": "무료나눔",
"image": "이미지",
"bargain": "가격제안 여부",
"place": "장소",
"category: "카테고리",
"views": "조회수",
"transaction_status": "거래 상태",
"refreshed_at": "끌어올리기",
"is_hide": "숨기기",
"bookmark": "관심등록",
"created_at": "생성일",
"updated_at": "수정일",
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


# 상품 카테고리
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
