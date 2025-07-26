from django.contrib.auth import get_user_model
from rest_framework import permissions

from apps.advertisement.models import AdvertisementModel
from apps.dealership.models import DealershipModel
from apps.dealership_staff.models import DealershipStaffModel

UserModel = get_user_model()

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_active and user.is_authenticated and user.is_admin)

class SellerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and setattr(request.user, 'is_seller', False)


class PremiumSellerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and setattr(request.user, 'is_seller', False) and (
                request.user.account_type == 'premium')


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser and request.user.is_active and request.user.is_staff)


class IsDealershipAccount(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_active and request.user.is_authenticated and request.user.account_type == "dealership")


class CanCreateAds(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or not user.is_active:
            return False
        if user.user_type == 'seller':
            return True

        staff = DealershipStaffModel.objects.filter(info=user, can_create_ads=True).select_related('dealership').first()

        if not staff:
            return False

        return DealershipModel.objects.filter(id=staff.dealership.id).exists()

class CanUpdateDeleteAds(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        ads_id = view.kwargs.get("pk")
        if not user.is_authenticated or not user.is_active:
            return False
        if user.user_type == 'seller' and AdvertisementModel.objects.filter(seller=user, id=ads_id):
            return True

        staff = DealershipStaffModel.objects.filter(info=user, can_create_ads=True).select_related('dealership').first()

        if not staff:
            return False

        return DealershipModel.objects.filter(id=staff.dealership.id).exists()

class CanHireStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_active or not user.is_authenticated:
            return False

        return bool(DealershipStaffModel.objects.filter(info=user, can_hire_workers=True).exists())


class CanChangeDealershipStaffRights(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated or not user.is_active:
            return False
        staff = DealershipStaffModel.objects.filter(info=user, can_hire_workers=True).first()
        if not staff:
            return False

        target_user_id = view.kwargs.get('pk') or request.data.get('user_id')
        if not target_user_id:
            return False

        try:
            target_user = UserModel.objects.get(id=target_user_id)
            target_staff = DealershipStaffModel.objects.get(info=target_user)
        except (UserModel.DoesNotExist, DealershipStaffModel.DoesNotExist):
            return False

        return staff.dealership_id == target_staff.dealership_id
