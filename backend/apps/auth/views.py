from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.user.serializer import UserSerializer
from core.services.jwt_service import JWTService, ActivateToken


class ActivateUserApiView(GenericAPIView):

    permission_classes = (AllowAny,)

    def patch(self, request, *args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.verify_token(token=token,token_class= ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

