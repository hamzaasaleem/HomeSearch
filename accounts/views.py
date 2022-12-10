from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
User=get_user_model()

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
        instance = serializer.save()
        if instance.role == 'agent':
            Agent.objects.get_or_create(user=instance)
        elif instance.role == 'customer':
            Customer.objects.get_or_create(user=instance)
        instance.save()



class ResetPasswordview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def partial_update(self, request, pk=None):
        # import pdb
        # pdb.set_trace()
        user = User.objects.get(id=request.user.id)
        if request.data['newPassword'] == request.data['confirmPassword']:
            if request.data['currPassword'] != request.data['newPassword']:

                if user.check_password(request.data['currPassword']):
                    user.set_password(request.data['newPassword'])
                    user.save()
                    return Response(
                        {"msg": "Password Updated Successfully"},
                        status=status.HTTP_200_OK
                    )
                return Response(
                    {"msg": "Password does not matched"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return Response(
                    {"msg": "You cannot use your current password again "},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"msg": "Password and Confirm Password Does not match"},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserRegistration(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        import pdb;pdb.set_trace()
        user_data = {
            'email': request.data['email'],
            # 'password': request.data['password'],
            'password': make_password(request.data['password']),
            'username': request.data['username'],
            'role': request.data['role'],
        }

        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=user_data['username'])
            user.password=make_password(request.data['password'])
            user.save()
            profile_data = {
                'user': str(user.id),
                'name': request.data['name'],
                'phone': request.data['phone'],
                'city': request.data['city'],
            }
            profileSerializer = None
            if user.role == 'agent':
                profileSerializer = AgentProfileSerializer(data=profile_data)
            elif user.role == 'customer':
                profileSerializer = CustomerProfileSerializer(data=profile_data)

            if profileSerializer.is_valid():
                profileSerializer.save()
                return Response(
                    {"msg": "User Created!"},
                    status=status.HTTP_201_CREATED)
            return Response(profileSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



