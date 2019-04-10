from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    """
    Non-authenticated users only
    """

    message = "You are already authenticated. Please, log out to try again."

    def has_permission(self, request, view):
        return not request.user.is_authenticated()  # request.user.is_autenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    message = "You must be the owner of this content to change."

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # if obj.user == request.user:
        #     return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
