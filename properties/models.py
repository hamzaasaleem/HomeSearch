from django.db import models
from accounts.models import Agent


# Create your models here.

class PropertyModel(models.Model):
    HOMES = 'homes'
    PLOTS = 'plots'
    COMMERCIAL = 'commercial'
    PROPERTY_TYPE = (
        (HOMES, 'Homes'),
        (PLOTS, 'Plots'),
        (COMMERCIAL, 'Commercial'),
    )

    SALE = 'sale'
    RENT = 'rent'
    PURPOSE = (
        (SALE, 'Sale'),
        (RENT, 'Rent'),
    )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=100, choices=PURPOSE)
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE)
    city = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    area = models.IntegerField(default='')
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    listing_expiry = models.IntegerField(default=0)
    monthly_rent = models.IntegerField(default=0)
    advance_rent = models.IntegerField(default=0)
    contact_person = models.CharField(max_length=100, default='')
    contact_person_email = models.CharField(max_length=100, default='')
    contact_person_phone = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
