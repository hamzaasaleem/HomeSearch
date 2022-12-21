from django.db import models
from accounts.models import Agent


# Create your models here.

# class PropertyModel(models.Model):
#     HOMES = 'homes'
#     PLOTS = 'plots'
#     COMMERCIAL = 'commercial'
#     PROPERTY_TYPE = (
#         (HOMES, 'Homes'),
#         (PLOTS, 'Plots'),
#         (COMMERCIAL, 'Commercial'),
#     )
#
#     SALE = 'sale'
#     RENT = 'rent'
#     PURPOSE = (
#         (SALE, 'Sale'),
#         (RENT, 'Rent'),
#     )
#     agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
#     purpose = models.CharField(max_length=100, choices=PURPOSE,null=True,blank=True)
#     installment = models.CharField(max_length=100, default='1.5',null=True,blank=True)
#     property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE,null=True,blank=True)
#     city = models.CharField(max_length=100, default='',null=True,blank=True)
#     address = models.CharField(max_length=100, default='',null=True,blank=True)
#     area = models.CharField(max_length=100, default='',null=True,blank=True)
#     bedrooms = models.CharField(max_length=100, default='',null=True,blank=True)
#     bathrooms = models.CharField(max_length=100, default='',null=True,blank=True)
#     listing_expiry = models.CharField(max_length=100, default='',null=True,blank=True)
#     monthly_rent = models.CharField(max_length=100, default='',null=True,blank=True)
#     advance_rent = models.CharField(max_length=100, default='',null=True,blank=True)
#     contact_person = models.CharField(max_length=100, default='',null=True,blank=True)
#     contact_person_email = models.CharField(max_length=100, default='',null=True,blank=True)
#     contact_person_phone = models.CharField(max_length=100, default='',null=True,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
#     updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

class BaseModel(models.Model):
    # HOMES = 'homes'
    # PLOTS = 'plots'
    # COMMERCIAL = 'commercial'
    # PROPERTY_TYPE = (
    #     (HOMES, 'Homes'),
    #     (PLOTS, 'Plots'),
    #     (COMMERCIAL, 'Commercial'),
    # )

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    # purpose = models.CharField(max_length=100, choices=PURPOSE, null=True, blank=True)
    # property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE, null=True, blank=True)
    city = models.CharField(max_length=100, default='', null=True, blank=True)
    address = models.CharField(max_length=100, default='', null=True, blank=True)
    area = models.CharField(max_length=100, default='', null=True, blank=True)
    listing_expiry = models.CharField(max_length=100, default='', null=True, blank=True)
    contact_person = models.CharField(max_length=100, default='', null=True, blank=True)
    contact_person_email = models.CharField(max_length=100, default='', null=True, blank=True)
    contact_person_phone = models.CharField(max_length=100, default='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class RentModel(BaseModel):
    monthly_rent = models.IntegerField(default=0, null=True, blank=True)
    advance_rent = models.IntegerField(default=0, null=True, blank=True)
    purpose = models.CharField(max_length=100, null=True, blank=True, default='rent')


class HomeRentModel(RentModel):
    bedrooms = models.IntegerField(default=0, null=True, blank=True)
    bathrooms = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.agent}'


class PlotRentModel(RentModel):
    # same as base
    def __str__(self):
        return f'{self.agent}'


class CommercialRentModel(RentModel):
    # same as base
    def __str__(self):
        return f'{self.agent}'


class SaleModel(BaseModel):
    installment = models.CharField(max_length=100, default='1.5', null=True, blank=True)
    price = models.CharField(max_length=100, default='0', null=True, blank=True)
    purpose = models.CharField(max_length=100, null=True, blank=True, default='sale')



class HomeSaleModel(SaleModel):
    bedrooms = models.CharField(max_length=100, default='', null=True, blank=True)
    bathrooms = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return f'{self.agent}'

class PlotSaleModel(SaleModel):
    def __str__(self):
        return f'{self.agent}'

class CommercialSaleModel(SaleModel):
    def __str__(self):
        return f'{self.agent}'
