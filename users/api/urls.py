from django.urls import path
from users.api.views import RegisterAPIView, LoginAPIView

app_name = "users_api"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
