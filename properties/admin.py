from django.contrib import admin
from properties.models import *


# Register your models here.
@admin.register(PropertyModel)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['agent', 'property_type', 'purpose', 'city']
