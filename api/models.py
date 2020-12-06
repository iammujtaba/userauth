from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
from django.core.validators import MinLengthValidator


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254,unique=True)
    is_email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    dob = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[MinLengthValidator(8)])
    is_phone_verified = models.BooleanField(default=False)
    image = models.TextField(null=True, blank=True)
    other_info = models.TextField(null=True, blank=True)
    is_blocked = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    signup_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','username']

    def __str__(self):
        return "{}".format(self.email)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"user_{self.email.split('@')[0]}"
        return super().save(*args, **kwargs)