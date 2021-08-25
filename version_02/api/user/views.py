from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from api.user.models import User
from api.user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """
    Create New User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)


class ManageUserView(RetrieveUpdateAPIView):
    """
    Retrieve and Update User
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        test = super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)




