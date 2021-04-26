from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif (request.user.is_anonymous and request.method != ['POST',
              'DELETE', 'PATCH']):
            return True
        elif request.user.role == 'admin':
            return True
        else:
            return False
