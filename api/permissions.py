from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User


class IsModeratorOrAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.role == request.user.is_moderator\
                and request.method == 'DELETE':
            return True
        else:
            return obj.author == request.user


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif (request.user.is_anonymous and request.method != ['POST',
              'DELETE', 'PATCH']):
            return True
        elif request.user.role == User.Role.ADMIN:
            return True
        else:
            return False
