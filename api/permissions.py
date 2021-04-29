from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModeratorOrAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_moderator\
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
        elif request.user.is_admin:
            return True
        else:
            return False
