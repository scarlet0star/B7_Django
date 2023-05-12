from rest_framework import serializers
from product.models import Product, ProductCategory, ProductImage


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


# 상품 이미지 생성 시리얼라이저
class ProductImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


# 상품 피드
class ProductFeedSerializer(serializers.ModelSerializer):
    images = ProductImageCreateSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = "__all__"


# 상품 등록
class ProductCreateSerializer(serializers.ModelSerializer):
    images = ProductImageCreateSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ("title", "content", "price", "is_free", "images",
                  "bargain", "place", "category", "refreshed_at", "is_hide",)
    
    def create(self, validated_data):
        print(validated_data)
        images_data = self.context.get('images', None)
        # images_data = validated_data.pop('images', None)
        product = super().create(validated_data)
        if images_data:
            for image_data in images_data:
                print(images_data)
                print(type(images_data))
                print(image_data)
                print(type(image_data))
                ProductImage.objects.create(product=product, image=image_data)
                # ProductImage.objects.create(product=product, **image_data)
        return product


# 상품 카테고리
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

