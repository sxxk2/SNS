from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from apps.utils.timestamp import TimeStampedModel


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        if not name:
            raise ValueError("계정 이름을 입력해주세요.")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, TimeStampedModel):
    email = models.EmailField(unique=True)
    name = models.CharField("계정의 이름", max_length=50, unique=True)
    mobile = models.CharField(max_length=20, null=True)
    profile_image = models.CharField(max_length=255, null=True)
    is_verified = models.BooleanField("공식 계정 여부", default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "accounts"
