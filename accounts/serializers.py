from rest_framework import serializers
from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source="role", write_only=True, allow_null=True,
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role", "role_id"]
        extra_kwargs = {"password": {"write_only": True}}


class UserCreateSerializer(UserSerializer):
    """Used by Djoser for registration"""

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
