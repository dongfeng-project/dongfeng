from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserLoginView(APIView):
    authentication_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(status=status.HTTP_200_OK, data={"detail": "both username and password are required"})

        user = authenticate(username=username, password=password)
        if user:
            login(request=request, user=user)
            return Response(status=status.HTTP_200_OK, data={"detail": "login success"})
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={"detail": "invalid username or password"})
