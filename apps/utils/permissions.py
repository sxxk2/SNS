from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_active:
            return False
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if request.user.is_admin:
                return True
            elif request.user.id == obj.id:
                return True
            else:
                return False
