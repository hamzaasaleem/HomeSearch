from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'gender']


class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'bio', 'phone', 'address', 'city']


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'bio', 'phone', 'address', 'city']


class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
