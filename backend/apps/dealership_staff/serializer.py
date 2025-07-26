from rest_framework.serializers import Serializer, ModelSerializer

from apps.dealership.serializer import DealershipSerializer
from apps.dealership_staff.models import DealershipStaffModel
from apps.user.serializer import UserSerializer


class DealershipStaffSerializer(ModelSerializer):
    info = UserSerializer()
    dealership=DealershipSerializer(read_only=True)
    class Meta:
        model = DealershipStaffModel
        fields = ('id','info','role','created_at','updated_at','can_create_ads','dealership')
        read_only_fields = ('id','info','created_at','role','updated_at','can_create_ads','dealership')