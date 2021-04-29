from rest_framework import permissions


class IsADM(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return bool(
                (request.user and request.user.is_staff)
                or (request.user and request.user.is_admin))
