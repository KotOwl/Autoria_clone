from django.urls import path

from apps.dealership_staff.views import CreateDealershipStaffApiView, HireDealershipStaffApiView, \
    MakeDealershipStaffAdmin

urlpatterns=[
    path('/create', CreateDealershipStaffApiView.as_view()),
    path('/hire',HireDealershipStaffApiView.as_view()),
    path('/make_admin/<int:pk>',MakeDealershipStaffAdmin.as_view())
]