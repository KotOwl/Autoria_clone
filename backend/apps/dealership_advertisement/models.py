import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.dealership.models import DealershipModel
from core.models import BaseModel


class DealershipAdvertisementModel(BaseModel):
    class Meta:
        db_table = 'dealership_advertisement'

    price = models.FloatField()
    watches = models.IntegerField()
    region = models.CharField(max_length=100)
    brand = models.CharField(max_length=120)
    model_of_car = models.CharField(max_length=120)
    car_year=models.IntegerField( validators=[
            MinValueValidator(1886),
            MaxValueValidator(datetime.datetime.now().year)
        ])
    description_of_car = models.CharField(max_length=700)
    seller = models.ForeignKey(DealershipModel, on_delete=models.CASCADE, related_name='seller', blank=True)

class DealershipCarImageModel(BaseModel):
    class Meta:
        db_table = 'dealership_images'

    image_of_car = models.ImageField(upload_to='images',blank=True)
    advertisement = models.ForeignKey(
        DealershipAdvertisementModel,
        on_delete=models.CASCADE,
        related_name='images',
        blank=True
    )