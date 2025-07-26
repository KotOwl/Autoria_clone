from rest_framework import serializers


from apps.dealership.models import DealershipModel
from apps.user.serializer import UserSerializer


class DealershipSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)


    class Meta:
        model = DealershipModel
        fields = ('id', 'name', 'owner','created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at', "owner")
