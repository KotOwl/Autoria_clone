from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from apps.auth.views import ActivateUserApiView

urlpatterns = [
    path('',TokenObtainPairView.as_view()),
    path('',TokenRefreshView.as_view()),
    path('/activate/<str:token>',ActivateUserApiView.as_view())
]