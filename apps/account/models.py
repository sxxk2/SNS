from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from apps.utils import TimeStampedModel


class UserManager(BaseUserManager):
    def create_user(self, email, account_name, password=None):
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        if not account_name:
            raise ValueError("계정 이름을 입력해주세요.")
        user = self.model(
            email=self.normalize_email(email),
            account_name=account_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, account_name, password=None):
        user = self.create_user(
            email,
            password=password,
            account_name=account_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, TimeStampedModel):
    # required
    email = models.EmailField(unique=True)
    account_name = models.CharField("계정의 이름", max_length=50, unique=True, blank=True, null=True)
    # password = models.CharField(_("password"), max_length=128) inherited from AbstractBaseUser

    # optional
    user_name = models.CharField("사용자의 이름", max_length=30, null=True)
    mobile = models.CharField(max_length=20, null=True)
    bio = models.CharField("소개", max_length=100, null=True)
    website = models.CharField(max_length=50, null=True)
    profile_image = models.CharField(max_length=255, null=True)

    # status
    is_verified = models.BooleanField("공식 계정 여부", default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    """
    inherited from TimeStampedModel
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    """
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["account_name"]

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
