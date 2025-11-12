from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    """Allow access only to admins or the user themselves."""
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
