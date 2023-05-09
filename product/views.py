from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from product.serializers import ProductFeedSerializer, ProductCreateSerializer, ProductCategorySerializer
from product.models import Product, ProductCategory

# 페이지네이션 import
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


# 페이지네이션
# 많이
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    # page_size_query_param = 'page_size'
    # max_page_size = 10000


# 보통
class StandardResultsSetPagination(PageNumberPagination):
    """
    마무리할때 size조정 필요
    """
    page_size = 20
    # page_size_query_param = 'page_size'
    # max_page_size = 1000


# 판매중 상품 피드 페이지
class ProductFeedView(generics.ListAPIView):
    queryset = Product.objects.filter(
        transaction_status=0).order_by('-refreshed_at')
    serializer_class = ProductFeedSerializer
    pagination_class = StandardResultsSetPagination

    """
    # 마지막 출력페이지 값
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        last_page = response.data['count'] // self.pagination_class.page_size
        print(last_page)
        return response
    """


# # 판매중 상품 피드 페이지
# class ProductFeed(APIView):
#     def get(self, request):
#         products = Product.objects.filter(
#             transaction_status=0).order_by('-refreshed_at')
#         serializer = ProductFeedSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# 상품 등록
# user_id 넣기
class ProductCreateView(APIView):
    def post(self, request):
        # user = get_object_or_404(User, id=user_id)
        # if request.user == user:
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
            # return Response({"message": "권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)


# 상품 자세히보기 수정 삭제
class ProductDetailView(APIView):

    # 자세히보기
    # user_id 넣기
    def get(self, request, product_id):
        # user = get_object_or_404(User, id=user_id)
        # if request.user == user:
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductFeedSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 수정
    # user_id 넣기
    def put(self, request, product_id):
        pass

    # 삭제
    # user_id 넣기
    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        product.delete()
        return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

        # # 작성자만 삭제 가능하게
        # if request.user == product.user:
        #     product.delete()
        #     return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     return Response({"message": "권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)


# 상품 카테고리 페이지
class ProductCategoryView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.filter(is_used=True)
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
