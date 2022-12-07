from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import *
from .serializers import *


class PropertyViewset(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.id
        agent = Agent.objects.get(user=user_id)
        request.data['agent'] = agent.id
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    # def list(self,request):
    #     property =PropertyModel.objects.filter(request['city']).filter(request['location']).filter(request['bedrooms'])
