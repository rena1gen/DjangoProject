from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и возвращает нового пользователя с заданным email и паролем.
        """
        if not email:
            raise ValueError('Email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
class MyTask(models.Model):
    message = models.CharField()
    user = models.ForeignKey(MyUser,  on_delete=models.CASCADE)
    created_date = models.CharField(default= 0)
    due_date = models.DateField()
    is_overdue = models.BooleanField(default=False)
    def __str__(self):
        return self.message+ ' '+str(self.due_date)


class Order(models.Model):
    email = models.ForeignKey(MyUser , on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
