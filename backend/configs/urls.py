"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path,include

from configs import settings

urlpatterns = [

    path('api/user',include('apps.user.urls')),
    path('api/auth',include('apps.auth.urls')),
    path('api/ads',include("apps.advertisement.urls")),
    path('api/dealership',include('apps.dealership.urls')),
    # path('api/dealership_ads',include('apps.dealership_advertisement.urls')),
    path('api/dealership_staff',include('apps.dealership_staff.urls')),
    path('api/cars',include('apps.cars.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)