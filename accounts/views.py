from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        user = request.user
        serializer = UserSerializer(user)
        if user.role == 'agent':
            current_user = AgentProfileSerializer(Agent.objects.get(user_id=user.id))
        elif user.role == 'customer':
            current_user = CustomerProfileSerializer(Customer.objects.get(user_id=user.id))

        dict_data = serializer.data | current_user.data

        return Response(dict_data)

    def update(self, request, pk=None):
        user_id = request.user.id
        user_data = {

            'email': request.data['email'],
            'gender': request.data['gender']
        }

        profile_data = {
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'bio': request.data['bio'],
            'phone': request.data['phone'],
            'address': request.data['address'],
            'city': request.data['city'],
            'user_image': request.data['user_image'],
        }
        profile = None
        if request.user.role == 'agent':
            agent = Agent.objects.get(user_id=user_id)
            profile = AgentProfileSerializer(agent, data=profile_data, partial=True)
        if request.user.role == 'customer':
            customer = Customer.objects.get(user_id=user_id)
            profile = CustomerProfileSerializer(customer, data=profile_data, partial=True)

        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=user_data, partial=True)
        if serializer.is_valid() and profile.is_valid():
            serializer.save()
            profile.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        import pdb;pdb.set_trace()
        instance = serializer.save()
        if instance.role == 'agent':
            Agent.objects.get_or_create(user=instance)
        elif instance.role == 'customer':
            Customer.objects.get_or_create(user=instance)
        instance.save()
