from django.contrib import admin
from properties.models import *


# Register your models here.
@admin.register(HomeRentModel)
class HomeRentModelAdmin(admin.ModelAdmin):
    list_display = ['agent', 'purpose', 'city','created_at']

@admin.register(PlotRentModel)
class HomeRentModelAdmin(admin.ModelAdmin):
    list_display = ['agent', 'purpose', 'city','created_at']

@admin.register(CommercialRentModel)
class HomeRentModelAdmin(admin.ModelAdmin):
    list_display = ['agent', 'purpose', 'city','created_at']


@admin.register(HomeSaleModel)
class HomeSaleModelAdmin(admin.ModelAdmin):
    list_display = ['agent', 'purpose', 'city', 'created_at']


@admin.register(PlotSaleModel)
class HomeSaleModelAdmin(admin.ModelAdmin):
    list_display = ['agent', 'purpose', 'city', 'created_at']

@admin.register(CommercialSaleModel)
class HomeSaleModelAdmin(admin.ModelAdmin):
    list_display = ['agent', 'purpose', 'city', 'created_at']