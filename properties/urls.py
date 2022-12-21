from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'rent-home', HomeRentViewset)
router.register(r'rent-plot', PlotRentViewset)
router.register(r'rent-commercial', CommercialRentViewset)


router.register(r'sale-home', HomeSaleViewset)
router.register(r'sale-plot', PlotSaleViewset)
router.register(r'sale-commercial', CommercialSaleViewset)

router.register(r'get-auth-properties', listAuthPropertiesViewset)

router.register(r'get-all-properties', listAllPropertiesViewset)

# router.register(r'sale', SaleViewset)

urlpatterns = [
    path('properties/', include(router.urls)),
    path('properties/agent/<int:pk>/', AgentsData),
    #Rent
    path('properties/home-rent/', PropertyHomeRentList.as_view()),
    path('properties/plot-rent/', PropertyPlotRentList.as_view()),
    path('properties/commercial-rent/', PropertyCommercialRentList.as_view()),
    #Sale
    path('properties/home-sale/', PropertyHomeSaleList.as_view()),
    path('properties/plot-sale/', PropertyPlotSaleList.as_view()),
    path('properties/commercial-sale/', PropertyCommercialSaleList.as_view()),
]
