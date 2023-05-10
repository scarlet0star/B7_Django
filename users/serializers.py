from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']


class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.set_password(validated_data.get(
            'password', instance.password))
        instance.save()
        return instance


class UserFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = self.user.name
        return data
