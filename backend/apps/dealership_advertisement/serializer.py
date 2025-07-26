

from rest_framework.serializers import ModelSerializer
from apps.dealership_advertisement.models import DealershipCarImageModel, DealershipAdvertisementModel


class DealershipCarImageSerializer(ModelSerializer):

    class Meta:
        model=DealershipCarImageModel
        fields=('id','image_of_car','created_at', 'updated_at')
        read_only_fields=('id','created_at', 'updated_at' )



class DealershipAdvertisementSerializer(ModelSerializer):
    images = DealershipCarImageSerializer(read_only=True, many = True)

    class Meta:
        model = DealershipAdvertisementModel
        fields = ('id', 'price', "watches", 'region',
                  'brand',
                  'model_of_car', 'images',
                  "description_of_car",
                   'created_at', 'updated_at')
        read_only_fields = ('id',  'created_at', 'updated_at',"seller",)

