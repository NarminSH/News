from django.http.response import JsonResponse
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth import authenticate
from users.models import User
from users.api.serializers import LoginSerializer, RegisterSerializer


class RegisterAPIView(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    model = User

    serializer_class = RegisterSerializer

    def post(self, *args, **kwargs):
        register_data = self.request.data
        serializer = RegisterSerializer(
            data=register_data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)


class LoginAPIView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        user = authenticate(username=username, password=password)

        if user:
            print("user", user.token)
            serializer = self.serializer_class(user)

            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(
            {"message": "Invalid credentials, try again"}, status=status.HTTP_200_OK
        )
