from django.urls import path

from apps.user.views import UserCreateApiView, MakeUserStaffApiView

urlpatterns = [
    path('',UserCreateApiView.as_view()),
    path('/make_staff/<int:pk>',MakeUserStaffApiView.as_view())

]