from rest_framework import viewsets
from api.models import User
from api.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

