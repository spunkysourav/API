from rest_framework import viewsets
from rest_framework import permissions
from.models import *
from.serializers import *
from rest_framework.exceptions import PermissionDenied
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner==request.user
class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    permission_classes=(IsOwner,)
    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            return User.objects.filter(owner=user)
        raise PermissionDenied()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# Create your views here.