from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'create-users', UserRegistration)
router.register(r'reset-password', ResetPasswordview)


urlpatterns = [
    path('accounts/', include(router.urls)),

    path('accounts/agents/', listAgents),

]
