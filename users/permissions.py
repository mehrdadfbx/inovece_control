from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        User = request.user
        return bool(User and User.is_authenticated and User.role == 'admin')