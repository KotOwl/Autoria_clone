from rest_framework.serializers import ModelSerializer

from apps.cars.models import ModelOfCarModel, CarsBrandModel


class BrandCarSerializer(ModelSerializer):
    class Meta:
        model = CarsBrandModel
        fields = ('id','brand','created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class CarsModelSerializer(ModelSerializer):
    brand = BrandCarSerializer(required=True)
    class Meta:
        model= ModelOfCarModel
        fields=('id','brand','model','created_at', 'updated_at')
        read_only_fields = ('id','created_at', 'updated_at')