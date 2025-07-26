from core.models import BaseModel
from django.db import models




class CarsBrandModel(BaseModel):
    class Meta:
        db_table = 'cars_brand'
    brand = models.CharField(max_length=20,unique=True)


class ModelOfCarModel(BaseModel):
    class Meta:
        db_table='cars_model'
    brand = models.ForeignKey(CarsBrandModel,on_delete=models.CASCADE,related_name='brand_of_car')
    model = models.CharField(max_length=60)