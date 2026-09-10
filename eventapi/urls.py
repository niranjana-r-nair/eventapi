"""
URL configuration for eventapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

from accounts.views import RegisterAPI,LogoutAPI
from events.views import EventAPI
from bookings.views import BookingAPIView,Verifypayment
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('user',RegisterAPI)
router.register('event',EventAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('login/',obtain_auth_token),
path('logout/', LogoutAPI.as_view()),
    path('booking/', BookingAPIView.as_view()),
    path('verify/', Verifypayment.as_view()),

]
