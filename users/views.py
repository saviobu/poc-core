from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    