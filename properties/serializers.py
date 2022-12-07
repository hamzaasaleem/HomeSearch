from rest_framework import serializers
from properties.models import *


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyModel
        fields = '__all__'
