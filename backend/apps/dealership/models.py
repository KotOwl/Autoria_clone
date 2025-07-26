from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

UserModel = get_user_model()


class DealershipModel(BaseModel):
    class Meta:
        db_table='dealership'
    owner = models.OneToOneField(UserModel , on_delete=models.CASCADE ,related_name='owner')
    name = models.CharField(max_length=50)






