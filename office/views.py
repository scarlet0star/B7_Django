from django.utils import timezone
from django.db.models.functions import TruncDate
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from product.models import Product, ProductCategory
from product.serializers import *

from .serializers import *

User = get_user_model()


class UserWriteCount(APIView):
    def get(self, request):
        users = User.objects.annotate(
            num_products=Count('product', distinct=True),
            num_posts=Count('post_set', distinct=True),
            num_comments=Count('comment_set', distinct=True)
        )
        user_data = {}
        for user in users:
            user_data[user.email] = [user.num_products, user.num_posts,
                                     user.num_comments]
       
        return Response(user_data)


class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all().order_by("-views")
        serializer = ProductFeedSerializer(product, many=True)
        return Response(serializer.data)


class ProductCountView(APIView):
    def get(self, request):
        week_ago = timezone.now() - timezone.timedelta(days=7)
        product_counts = (
            Product.objects
            .filter(created_at__gte=week_ago)
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )
        data = {
            'dates': [str(item['date']) for item in product_counts],
            'counts': [item['count'] for item in product_counts],
        }
        return Response(data)


class CategoryProductCountAPIView(APIView):
    def get(self, request, format=None):
        categories = ProductCategory.objects.annotate(
            products=Count('product'))
        data = {category.name: category.products for category in categories}
        return Response(data)


class TransactionStatusCountAPIView(APIView):
    def get(self, request, format=None):
        transaction_statuses = [0, 1, 2]  # 거래 상태 코드
        status_names = ["판매중", "예약중", "판매완료"]  # 거래 상태 이름
        data = {}

        for status, name in zip(transaction_statuses, status_names):
            count = Product.objects.filter(transaction_status=status).count()
            data[name] = count

        return Response(data)


class ToggleIsAdmin(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        user = get_object_or_404(get_user_model(), pk=pk)
        data = {'is_admin': not user.is_admin}
        serializer = AdminSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToggleUserIsActive(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        user = get_object_or_404(get_user_model(), pk=pk)
        data = {'is_active': not user.is_active}
        serializer = AdminSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
