from rest_framework import serializers
from properties.models import *


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyModel
        exclude = ['agent']
