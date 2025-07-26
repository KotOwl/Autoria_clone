from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.advertisement.filter import AdvertisementFilter
from apps.advertisement.models import AdvertisementModel, CarImageModel
from apps.advertisement.serializer import AdvertisementSerializer, CarImageSerializer
from apps.advertisement.validation import validate_ads
from apps.dealership_staff.models import DealershipStaffModel
from core.permissions.permissions import SellerPermission, CanCreateAds, CanUpdateDeleteAds
from core.services.email_service import EmailService


class ListAdvertisementApiView(ListAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        return AdvertisementModel.objects.filter(advertisement_status='available')
class GetOneAdvertisementApiView(ListAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateAdvertisementApiView(CreateAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (CanCreateAds,)
    def post(self, request, *args, **kwargs):
        user = request.user


        if user.account_type == 'basic' and user.user_type == 'seller':
            ad_count = AdvertisementModel.objects.filter(seller=user).count()
            if ad_count >= 1:
                return Response(
                    {'detail': 'You need to buy a premium account to post more car advertisements.'},
                    status=status.HTTP_403_FORBIDDEN
                )


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        if user.user_type == 'dealership_staff':
            dealership_staff = DealershipStaffModel.objects.filter(info=user).first()
            ads = serializer.save(dealership=dealership_staff.dealership)
            ads.advertisement_status = 'available'
            ads.save(update_fields=['advertisement_status'])
        else:
            ads = serializer.save(seller=user)
            ads.advertisement_status = 'available'
            ads.save(update_fields=['advertisement_status'])


        status_of_ads, message = validate_ads(request.data)
        if not status_of_ads:
            ads.advertisement_status = 'not_complete'
            ads.failed_checks = 1
            ads.save(update_fields=['advertisement_status', 'failed_checks'])
            return Response(
                {'detail': 'Your ad was created, but users cannot see it yet. Reason: ' + message},
                status=status.HTTP_202_ACCEPTED
            )

        return Response(self.get_serializer(ads).data, status=status.HTTP_201_CREATED)

class CarAddImageView(UpdateAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['put']

    def put(self, request, *args, **kwargs):
        ads_pk = kwargs.get('pk')
        advertisement = AdvertisementModel.objects.filter(id=ads_pk).first()

        image_file = request.FILES.get('image_of_car')

        if not image_file:
            return Response({'detail': 'No image provided.'}, status=400)

        CarImageModel.objects.create(image_of_car=image_file, advertisement=advertisement)

        return Response({'detail': 'Image uploaded successfully.'})


class DeleteAdvertisementApiView(DestroyAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (SellerPermission,)

    def delete(self, request, *args, **kwargs):
        user = request.user
        ads = self.get_object()
        if user.is_staff:
            self.perform_destroy(ads)
            return Response("Advertisement is successfully deleted", status=status.HTTP_204_NO_CONTENT)

        if user != ads.seller:
            return Response("You cannot delete others advertisements", status=status.HTTP_405_METHOD_NOT_ALLOWED)

        self.perform_destroy(ads)
        return Response("Advertisement is successfully deleted", status=status.HTTP_204_NO_CONTENT)


class UpdateAdvertisementApiView(UpdateAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (CanUpdateDeleteAds,)

    def patch(self, request, *args, **kwargs):
        ad = self.get_object()
        fails = ad.failed_checks

        status_of_ads, message = validate_ads(request.data)
        if not status_of_ads:
            if fails == 2:
                EmailService.report_ads(ads=ad)
                ad.advertisement_status = 'unavailable'
                ad.save(update_fields=['advertisement_status'])
                return Response("Your advertisement is unavailable and we send letter to admin for re-checking it please wait until admin check it",status=status.HTTP_406_NOT_ACCEPTABLE)

            ad.failed_checks = fails + 1
            ad.save(update_fields=["failed_checks"])
            return Response({"error": message}, status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = self.get_serializer(ad, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        ad = serializer.save()
        ad.advertisement_status = 'available'
        ad.save(update_fields=['advertisement_status'])

        return Response(AdvertisementSerializer(ad).data, status=status.HTTP_200_OK)
