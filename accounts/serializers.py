from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
