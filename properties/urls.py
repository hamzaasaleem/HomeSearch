from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'property', PropertyViewset)

urlpatterns = [
    path('properties/', include(router.urls))
]
