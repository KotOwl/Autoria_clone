from django.contrib.auth import get_user, get_user_model

from apps.dealership.models import DealershipModel
from core.models import BaseModel
from django.db import models

UserModel = get_user_model()


class DealershipStaffModel(BaseModel):
    class Meta:
        db_table='dealership_staff'
    info = models.OneToOneField(UserModel,on_delete=models.CASCADE,related_name='staff_info')
    role = models.CharField(max_length=30)
    dealership = models.ForeignKey(DealershipModel,on_delete=models.CASCADE,related_name='dealership',blank=True, null=True)
    can_create_ads = models.BooleanField(default=False)
    can_hire_workers =models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    can_change_staff_rights = models.BooleanField(default=False)
