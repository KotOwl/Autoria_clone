from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.dealership.models import DealershipModel
from core.models import BaseModel
from core.services.file_service import upload_advertisement_photo

UserModel = get_user_model()




class AdvertisementModel(BaseModel):
    class Meta:
        db_table = 'advertisement'

    price = models.FloatField()
    watches = models.IntegerField()
    region = models.CharField(max_length=100)
    failed_checks= models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=120)
    model_of_car = models.CharField(max_length=120)
    car_year = models.IntegerField(validators=[
        MinValueValidator(1886),
        MaxValueValidator(datetime.now().year)
    ])
    advertisement_status = models.CharField(max_length=30,default='unavailable')
    description_of_car = models.CharField(max_length=700)
    seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_advertisements', blank=True,null=True)
    dealership = models.ForeignKey(DealershipModel, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="dealership_ads")

    def owner_type(self):
        if self.seller:
            return "user"
        elif self.dealership:
            return "dealership"
        return "unknown"


class CarImageModel(BaseModel):
    class Meta:
        db_table = 'images'

    image_of_car = models.ImageField(upload_to=upload_advertisement_photo,blank=True)
    advertisement = models.ForeignKey(
        AdvertisementModel,
        on_delete=models.CASCADE,
        related_name='images',
        blank=True
    )
