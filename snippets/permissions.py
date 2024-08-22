from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only owner to edit"""

    def has_object_permission(self, request, view, obj):
        print(type(obj))
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner
