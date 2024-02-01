
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import User
from apps.users.serializers import  UserRegisterSerializer, UserSerializer
from apps.users.permissions import UserPermissons

class UserAPIViewsSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermissons(),)
        return (AllowAny(), )
    
    def perform_update(self, serializer):
        return serializer.save(user = self.request.user)
    


