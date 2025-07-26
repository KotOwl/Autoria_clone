from rest_framework.urlpatterns import path

from apps.dealership.views import CreateDealershipApiView

urlpatterns = [
    path('/create',CreateDealershipApiView.as_view()),
]