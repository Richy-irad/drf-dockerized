from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it.

    Args:
        permissions (BasePermission): The base permission class from DRF.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # so we'll always allow GET request, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == self.request.user