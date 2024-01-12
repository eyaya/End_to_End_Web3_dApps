# backend urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.conf.urls import include

from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

