from logging import raiseExceptions

from rest_framework.generics import CreateAPIView

from apps.advertisement.models import AdvertisementModel
from apps.advertisement.serializer import AdvertisementSerializer
from apps.dealership.models import DealershipModel
from apps.dealership.serializer import DealershipSerializer
from apps.dealership_staff.models import DealershipStaffModel
from core.permissions.permissions import IsDealershipAccount
from rest_framework.response import Response
from rest_framework import status

class CreateDealershipApiView(CreateAPIView):
    serializer_class = DealershipSerializer
    queryset = DealershipModel.objects.all()
    permission_classes = (IsDealershipAccount,)

    def post(self, request, *args, **kwargs):
        user = request.user

        if not user.account_type == "dealership":
            return Response(data='You need to buy "dealership" subscribe to create your own dealership' ,status=status.HTTP_402_PAYMENT_REQUIRED)
        user.user_type = 'dealership_staff'
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dealership = serializer.save(owner=user)
        DealershipStaffModel.objects.create(
            dealership=dealership,
            info=user,
            role ='owner',
            can_create_ads=True,
            can_hire_workers=True,
            can_change_staff_rights=True,
            is_admin=True,



        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

