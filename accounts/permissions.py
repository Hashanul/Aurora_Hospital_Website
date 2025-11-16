from rest_framework.permissions import BasePermission, SAFE_METHODS



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




class NewsPermission(BasePermission):
    """
    - GET (list/retrieve) → Everyone (Anonymous + Authenticated)
    - POST/PUT/PATCH/DELETE → Only admin, staff, superuser
    """

    def has_permission(self, request, view):

        # Allow EVERYONE for GET/HEAD/OPTIONS
        if request.method in SAFE_METHODS:
            return True

        user = request.user

        # If not authenticated → block write requests
        if not user or not user.is_authenticated:
            return False

        # Allow write only to admin/staff/superuser
        return user.is_superuser or user.is_staff or getattr(user, "role", None) == "admin"
