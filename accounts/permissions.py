

from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    allowed_roles = ["admin"]

    def has_permission(self, request, view):
        user = request.user

        # Allow if user is not authenticated
        if not user.is_authenticated:
            return False

        # Allow superusers or staff automatically
        if user.is_staff or user.is_superuser:
            return True

        # Ensure the user has a role
        if not hasattr(user, "role") or not user.role:
            return False

        # Check if user's role is allowed
        return user.role.name in self.allowed_roles
