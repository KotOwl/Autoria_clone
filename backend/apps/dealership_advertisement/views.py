# from rest_framework import status
# from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
#
# from apps.dealership_advertisement.models import DealershipAdvertisementModel, DealershipCarImageModel
# from apps.dealership_advertisement.serializer import DealershipAdvertisementSerializer, DealershipCarImageSerializer
# from apps.dealership_staff.models import DealershipStaffModel
# from core.permissions.permissions import CanCreateDeleteAdsForDealership
#
# class ListDealershipAdvertisementApiView(ListAPIView):
#     serializer_class = DealershipAdvertisementSerializer
#     queryset = DealershipAdvertisementModel.objects.all()
#     permission_classes = (AllowAny,)
#
#
# class CreateDealershipAdsApiView(CreateAPIView):
#     serializer_class = DealershipAdvertisementSerializer
#     queryset = DealershipAdvertisementModel.objects.all()
#     permission_classes = ( CanCreateDeleteAdsForDealership,)
#     http_method_names = ['post']
#
#     def post(self, request, *args, **kwargs):
#         user = request.user
#         dealership_staff = DealershipStaffModel.objects.filter(info=user).first()
#         dealership = dealership_staff.dealership
#         serializer= self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(seller=dealership)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# class DealershipCarAddImageView(UpdateAPIView):
#     queryset = DealershipAdvertisementModel.objects.all()
#     serializer_class = DealershipCarImageSerializer
#     permission_classes = (AllowAny,)
#     http_method_names = ['put']
#
#     def put(self, request, *args, **kwargs):
#         ads_pk = kwargs.get('pk')
#         advertisement = DealershipAdvertisementModel.objects.filter(id=ads_pk).first()
#
#         image_file = request.FILES.get('image_of_car')
#
#         if not image_file:
#             return Response({'detail': 'No image provided.'}, status=400)
#
#         DealershipCarImageModel.objects.create(image_of_car=image_file, advertisement=advertisement)
#
#         return Response({'detail': 'Image uploaded successfully.'})
#
#
# class DeleteDealershipAdvertisementApiView(DestroyAPIView):
#     queryset = DealershipAdvertisementModel.objects.all()
#     serializer_class = DealershipAdvertisementSerializer
#     permission_classes = (CanCreateDeleteAdsForDealership,)
#
# class UpdateDealershipAdvertisementApiView(UpdateAPIView):
#     queryset = DealershipAdvertisementModel.objects.all()
#     serializer_class = DealershipAdvertisementSerializer
#
#
#
