from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from product.serializers import ProductFeedSerializer, ProductCreateSerializer
from product.models import Product, ProductCategory
from rest_framework.pagination import PageNumberPagination

# 페이지네이션 import
from rest_framework import generics


# 페이지네이션
# 많이
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


# 보통
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


# 판매중 상품목록
class ProductFeed(generics.ListAPIView):
    queryset = Product.objects.filter(
        transaction_status=0).order_by('-refreshed_at')
    serializer_class = ProductFeedSerializer
    pagination_class = StandardResultsSetPagination


# # 판매중 상품목록
# class ProductFeed(APIView):
#     def get(self, request):
#         products = Product.objects.filter(
#             transaction_status=0).order_by('-refreshed_at')
#         serializer = ProductFeedSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


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
