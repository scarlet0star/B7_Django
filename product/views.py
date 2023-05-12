from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from product.serializers import ProductFeedSerializer, ProductCreateSerializer, ProductCategorySerializer
from product.models import Product, ProductCategory
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.utils import timezone


# 상품 등록
"""로그인 사용자"""
class ProductCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data, context={"images":request.data.getlist("images")})
        print(request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 상품 자세히보기 수정 삭제
"""로그인 사용자"""
class ProductDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 자세히보기
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        
        # 보이기 상태일때
        if product.is_hide == False:
            serializer = ProductFeedSerializer(product)
            product.views += 1
            product.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # 숨기기 상태일때
        elif product.is_hide == True:
            if request.user == product.user:
                serializer = ProductFeedSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)

    # 수정
    def put(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        
        if request.user == product.user:
            # 끌어올리기
            if "refreshed_at" in request.data:
                product.refreshed_at = timezone.now()
                product.save()
                return Response({"message": "끌어올렸습니다!"}, status=status.HTTP_200_OK)

            # 내용 수정
            else:
                serializer = ProductCreateSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save(user=request.user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)

    # 삭제
    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        # 작성자만 삭제 가능하게
        if request.user == product.user:
            product.delete()
            return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)


# 페이지네이션
class StandardResultsSetPagination(PageNumberPagination):
    """
    마무리할때 size조정 필요
    """
    page_size = 20


# 판매중 상품 피드 페이지
"""모든 사용자"""
class ProductFeedView(generics.ListAPIView):
    queryset = Product.objects.filter(transaction_status=0, is_hide=False).order_by('-refreshed_at')
    serializer_class = ProductFeedSerializer
    pagination_class = StandardResultsSetPagination


# 상품 카테고리 정보
"""모든 사용자"""
class ProductCategoryView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.filter(is_used=True)
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 상품 카테고리별 필터 리스트
"""모든 사용자"""
class ProductCategoryFilterView(generics.ListAPIView):
    serializer_class = ProductFeedSerializer
    pagination_class = StandardResultsSetPagination

    # category_id 가져오기 위해 오버라이딩
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(ProductCategory, id=category_id)

        if category.name == "인기매물":
            queryset = Product.objects.filter(transaction_status=0, is_hide=False).order_by('-views')
            """거래중, 숨김상태 아님, 조회수 순서로"""
            return queryset
        else:
            queryset = Product.objects.filter(transaction_status=0, is_hide=False, category=category).order_by('-refreshed_at')
            """거래중, 숨김상태 아님, 해당 카테고리 상품만"""
            return queryset


# 관심상품 등록/제외
"""로그인 사용자"""
class ProductBookmarkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        me = request.user
        if me in product.bookmark.all():
            product.bookmark.remove(me)
            return Response("관심상품에서 제외했습니다.", status=status.HTTP_200_OK)
        else:
            product.bookmark.add(me)
            return Response("관심상품으로 등록했습니다.", status=status.HTTP_200_OK)


# 관심상품 리스트
"""로그인 사용자"""
class ProductBookmarkListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductFeedSerializer
    pagination_class = StandardResultsSetPagination

    # user_id 가져오기 위해 오버라이딩
    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Product.objects.filter(transaction_status=0, is_hide=False, bookmark=user_id).order_by('-refreshed_at')
        """거래중, 숨김상태 아님, 요청유저가 북마크한것만"""
        return queryset
