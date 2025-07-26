from django.urls import path

from apps.advertisement.views import CreateAdvertisementApiView, CarAddImageView, ListAdvertisementApiView, \
    UpdateAdvertisementApiView, GetOneAdvertisementApiView

urlpatterns = [
    path('/create', CreateAdvertisementApiView.as_view()),
    path('/image/<int:pk>', CarAddImageView.as_view()),
    path('/get', ListAdvertisementApiView.as_view()),
    path('/update/<int:pk>', UpdateAdvertisementApiView.as_view()),
    path('/get/<int:pk>',GetOneAdvertisementApiView.as_view())
]
