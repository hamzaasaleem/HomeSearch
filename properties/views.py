from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class PropertyViewset(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]
