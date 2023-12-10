from django.contrib.auth import authenticate, login
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


# Create your views here.
class UserLoginView(APIView):
    authentication_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED, data={"detail": "both username and password are required"}
            )

        user = authenticate(username=username, password=password)
        if user:
            login(request=request, user=user)
            return Response(status=status.HTTP_200_OK, data={"detail": "login success"})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "invalid username or password"})


class CurrentUserView(GenericAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get(self, request):
        serializer = self.serializer_class(self.get_object())
        return Response(status=status.HTTP_200_OK, data=serializer.data)
