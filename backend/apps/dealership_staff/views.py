from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.dealership.models import DealershipModel
from apps.dealership_staff.models import DealershipStaffModel
from apps.dealership_staff.serializer import DealershipStaffSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.user.serializer import UserSerializer
from core.permissions.permissions import CanHireStaff, CanChangeDealershipStaffRights

UserModel = get_user_model()


class CreateDealershipStaffApiView(CreateAPIView):
    serializer_class = DealershipStaffSerializer
    queryset = DealershipStaffModel.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user
        staff = DealershipStaffModel.objects.filter(info=user).first()
        if not staff:
            return Response({'detail': 'You are not a dealership staff.'}, status=403)
        dealership = get_object_or_404(DealershipModel, id=staff.dealership_id)
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        created_user = user_serializer.save()
        created_user.user_type = 'dealership_staff'
        created_staff = DealershipStaffModel.objects.create(
            info=created_user,
            dealership=dealership,

        )
        response_serializer = self.get_serializer(created_staff)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class HireDealershipStaffApiView(CreateAPIView):
    queryset = DealershipStaffModel.objects.all()
    serializer_class = DealershipStaffSerializer
    permission_classes = (CanHireStaff,)

    def post(self, request, *args, **kwargs):
        user_email = request.data.get('email')
        if not user_email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        dealership_staff = DealershipStaffModel.objects.filter(info=user).first()

        if not dealership_staff:
            return Response({"error": "Current user is not linked to any dealership."},
                            status=status.HTTP_400_BAD_REQUEST)

        staff = get_object_or_404(UserModel, email=user_email)

        if staff == dealership_staff.dealership.owner:
            return Response({"error": "Cannot add the dealership owner as staff."}, status=status.HTTP_400_BAD_REQUEST)

        if DealershipStaffModel.objects.filter(info=staff, dealership=dealership_staff.dealership).exists():
            return Response({"error": "User is already hired to this dealership."}, status=status.HTTP_400_BAD_REQUEST)
        staff.user_type = 'dealership_staff'
        staff.save(update_fields=['user_type'])
        hired_staff = DealershipStaffModel.objects.create(info=staff, dealership=dealership_staff.dealership)

        serializer = DealershipStaffSerializer(hired_staff)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class MakeDealershipStaffAdmin(UpdateAPIView):
    permission_classes = (CanChangeDealershipStaffRights,)
    serializer_class = DealershipStaffSerializer
    queryset = DealershipStaffModel.objects.all()

    def put(self, request, *args, **kwargs):
        staff_id = kwargs.get('pk')

        staff = DealershipStaffModel.objects.filter(id=staff_id).first()
        staff.is_admin=True
        staff.can_change_staff_rights=True
        staff.can_hire_workers=True
        staff.can_create_ads=True
        staff.save()

        return Response("User now is admin",status=status.HTTP_200_OK)

