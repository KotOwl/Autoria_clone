from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from apps.cars.models import CarsBrandModel, ModelOfCarModel
from apps.cars.serializer import BrandCarSerializer, CarsModelSerializer


class CreateCarBrandApiView(CreateAPIView):
    queryset = CarsBrandModel.objects.all()
    serializer_class = BrandCarSerializer
    permission_classes = (IsAdminUser,)


class GetCarsBrandApiView(ListAPIView):
    queryset = CarsBrandModel.objects.all()
    serializer_class = BrandCarSerializer
    permission_classes = (AllowAny,)


class CreateCarModelApiView(CreateAPIView):
    queryset = ModelOfCarModel.objects.all()
    serializer_class = CarsModelSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        brand = data.pop('brand', None)

        if not brand:
            return Response({"error": "Brand is required."}, status=400)

        car_brand = CarsBrandModel.objects.filter(brand=brand).first()
        if not car_brand:
            return Response({"error": "Brand not found."}, status=404)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(brand=car_brand)

        return Response(serializer.data, status=201)


class GetCarsModelApiView(ListAPIView):
    queryset = ModelOfCarModel.objects.all()
    serializer_class = CarsModelSerializer
    permission_classes = [AllowAny]


class MultiBrandCreateApiView(CreateAPIView):
    queryset = CarsBrandModel.objects.all()
    serializer_class = BrandCarSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        brands = data.get('brands', [])
        if not isinstance(brands, list):
            return Response({'error': '"brands" must be a list of brand objects'}, status=status.HTTP_400_BAD_REQUEST)

        created = []
        errors = []

        for brand_name in data['brands']:
            serializer = self.get_serializer(data={"brand": brand_name})
            if serializer.is_valid():
                serializer.save()
                created.append(serializer.data)
            else:
                errors.append(serializer.errors)

        if errors:
            return Response({'created': created, 'errors': errors}, status=status.HTTP_207_MULTI_STATUS)

        return Response({'message': 'All brands created successfully', 'data': created}, status=status.HTTP_201_CREATED)
