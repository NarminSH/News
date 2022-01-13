from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from datetime import datetime, timedelta
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    # moderations

    email = models.EmailField(("email address"))
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def token(self):
        token = jwt.encode(
            {
                "email": self.email,
                "username": self.username,
                "id": self.id,
                "exp": datetime.utcnow() + timedelta(hours=24),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )
        return token

    def __str__(self):
        return self.username
