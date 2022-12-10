from rest_framework import serializers
from properties.models import *


class HomeSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSaleModel
        fields = '__all__'


class PlotSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotSaleModel
        fields = '__all__'


class CommercialSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialSaleModel
        fields = '__all__'


class HomeRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeRentModel
        fields = '__all__'


class PlotRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotRentModel
        fields = '__all__'


class CommercialRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialRentModel
        fields = '__all__'
