from django.contrib.auth import get_user_model
from django.core.serializers import serialize
from rest_framework.generics import GenericAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.user.serializer import UserSerializer
from core.permissions.permissions import IsSuperUser
from rest_framework import status
UserModel = get_user_model()

class UserCreateApiView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class =UserSerializer
    permission_classes =(AllowAny,)

class MakeUserStaffApiView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, request, *args, **kwargs):

        user = self.get_object()
        if not user.is_staff:
            user.is_staff=True
            user.save()


        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)


