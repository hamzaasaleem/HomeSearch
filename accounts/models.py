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

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    role = models.CharField(choices=ROLES, max_length=50, default=CUSTOMER)
    gender = models.CharField(choices=GENDER, max_length=100, default=MALE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} [{self.get_role_display()}]"


class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='user_image/', null=True, blank=True, default='/media/user_image/placeholder.jpeg')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
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
