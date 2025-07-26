from rest_framework.urls import path

from apps.cars.views import GetCarsBrandApiView, CreateCarBrandApiView, CreateCarModelApiView, GetCarsModelApiView, \
    MultiBrandCreateApiView

urlpatterns=[
    path('/get/brand',GetCarsBrandApiView.as_view()),
    path('/create/brand',CreateCarBrandApiView.as_view()),
    path('/create/model',CreateCarModelApiView.as_view()),
    path('get/model',GetCarsModelApiView.as_view()),
    path('/multicreate',MultiBrandCreateApiView.as_view())
]