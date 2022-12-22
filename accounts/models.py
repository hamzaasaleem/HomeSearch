from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    CUSTOMER = 'customer'
    AGENT = 'agent'

    ROLES = (
        (CUSTOMER, 'Customer'),
        (AGENT, 'Agent')
    )


    role = models.CharField(choices=ROLES, max_length=50, default=CUSTOMER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} [{self.get_role_display()}]"


class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='user_image/', null=True, blank=True, default='/user_image/placeholder.jpeg')
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} [{self.user.get_role_display()}]"

    class Meta:
        abstract = True


class Agent(BaseProfile):

    def __str__(self):
        return f"{self.user.username} [{self.user.get_role_display()}]"


class Customer(BaseProfile):

    def __str__(self):
        return f"{self.user.username} [{self.user.get_role_display()}]"
