from rest_framework import serializers
from django.contrib.auth import get_user_model


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['is_active', 'is_admin']
