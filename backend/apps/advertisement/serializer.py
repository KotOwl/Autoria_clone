

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.advertisement.models import AdvertisementModel, CarImageModel
from apps.dealership.serializer import DealershipSerializer
from apps.user.serializer import UserSerializer

UserModel = get_user_model()

class CarImageSerializer(ModelSerializer):

    class Meta:
        model=CarImageModel
        fields=('id','image_of_car','created_at', 'updated_at')
        read_only_fields=('id','created_at', 'updated_at' )



class AdvertisementSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(read_only=True, many=True)
    owner = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = AdvertisementModel
        fields = (
            'id', 'price', 'watches', 'region', 'brand',
            'model_of_car', 'images', 'description_of_car',
            'created_at', 'updated_at', 'owner', 'type','failed_checks','car_year'
        )
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'owner', 'type', 'images','failed_checks'
        )


    def get_owner(self, obj):
        if obj.seller:
            return UserSerializer(obj.seller, context=self.context).data
        elif obj.dealership:
            return DealershipSerializer(obj.dealership, context=self.context).data
        return None

    def get_type(self, obj):
        return obj.owner_type()