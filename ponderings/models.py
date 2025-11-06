from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Pondering(BaseModel):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    private = models.BooleanField()

    def __str__(self):
        return self.content