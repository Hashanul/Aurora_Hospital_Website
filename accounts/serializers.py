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

        # Check if role is provided
        role = validated_data.pop("role", None)

        # If role is None, set default role "patient"
        if role is None:
            from .models import Role
            role = Role.objects.filter(name="patients").first()  # get patient role
            validated_data["role"] = role

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


# class CustomLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)


# permissions/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']

from rest_framework import serializers
from django.contrib.auth.models import User, Permission

class UserPermissionAssignSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    permission_ids = serializers.ListField(child=serializers.IntegerField())

    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User not found")
        return value

    def save(self):
        user = User.objects.get(id=self.validated_data['user_id'])
        permissions = Permission.objects.filter(id__in=self.validated_data['permission_ids'])
        
        user.user_permissions.set(permissions)  # overwrite
        # user.user_permissions.add(*permissions)  -> to append instead
        
        return user
