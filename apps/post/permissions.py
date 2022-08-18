from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_active:
            return False
        if user.is_admin:
            return True
        if request.method in SAFE_METHODS:
            return True

        if user.is_authenticated:
            if user.id == obj.writer.id:
                return True
            else:
                return False
