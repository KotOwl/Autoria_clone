
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from apps.user.managers import UserManager
from core.models import BaseModel
from django.db import models


class UserModel(AbstractBaseUser,BaseModel,PermissionsMixin):


    class Meta:
        db_table ='auth_user'

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    user_type = models.CharField(max_length=30,default='seller')
    account_type=models.CharField(max_length=10,default='basic')


    USERNAME_FIELD='email'

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table ='profile'

    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    age=models.IntegerField()

    user=models.OneToOneField(UserModel,on_delete=models.CASCADE,related_name='profile')


