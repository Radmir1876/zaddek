from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Email must be provided')

        if not username:
            raise ValueError('Username must be provided')

        user = self.model(
            email = self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    USER_ROLES = (
        ("Seller", "Seller"),
        ("buyer", "buyer"),
    )
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='Email Address',
                              unique=True,
                              max_length=40)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    role = models.CharField(choices=USER_ROLES, max_length=100, default='seller')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    objects = UserManager()
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True    

    def has_module_perms(self, app_label):
        return True   

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
