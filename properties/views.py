from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.serializers import AgentProfileSerializer
from .models import *
from .serializers import *


class HomeRentViewset(viewsets.ModelViewSet):
    queryset = HomeRentModel.objects.all()
    serializer_class = HomeRentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.id
        agent = Agent.objects.get(user=user_id)
        request.data['agent'] = agent.id
        serializer = HomeRentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class PlotRentViewset(viewsets.ModelViewSet):
    queryset = PlotRentModel.objects.all()
    serializer_class = PlotRentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.id
        agent = Agent.objects.get(user=user_id)
        request.data['agent'] = agent.id
        serializer = PlotRentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class CommercialRentViewset(viewsets.ModelViewSet):
    queryset = CommercialRentModel.objects.all()
    serializer_class = CommercialRentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.id
        agent = Agent.objects.get(user=user_id)
        request.data['agent'] = agent.id
        serializer = CommercialRentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class HomeSaleViewset(viewsets.ModelViewSet):
    queryset = HomeSaleModel.objects.all()
    serializer_class = HomeSaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.id
        agent = Agent.objects.get(user=user_id)
        request.data['agent'] = agent.id
        serializer = HomeSaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class PlotSaleViewset(viewsets.ModelViewSet):
    queryset = PlotSaleModel.objects.all()
    serializer_class = PlotSaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.id
        agent = Agent.objects.get(user=user_id)
        request.data['agent'] = agent.id
        serializer = PlotSaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class CommercialSaleViewset(viewsets.ModelViewSet):
    queryset = CommercialSaleModel.objects.all()
    serializer_class = CommercialSaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.id
        agent = Agent.objects.get(user=user_id)
        request.data['agent'] = agent.id
        serializer = CommercialSaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class listAuthProperties(viewsets.ModelViewSet):
    queryset = CommercialSaleModel.objects.all()
    serializer_class = CommercialSaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user_id = request.user.id
        agent_id = Agent.objects.get(user=user_id)

        try:
            rentedHomes = HomeRentModel.objects.get(agent=agent_id)
            rentedHomeserializer = HomeRentSerializer(rentedHomes)
        except:
            rentedHomeserializer = None

        try:
            rentedPlots = PlotRentModel.objects.get(agent=agent_id)
            rentedPlotserializer = HomeRentSerializer(rentedPlots)
        except:
            rentedPlotserializer = None

        try:
            rentedCommerical = CommercialRentModel.objects.get(agent=agent_id)
            rentedCommercialserializer = HomeRentSerializer(rentedCommerical)
        except:
            rentedCommercialserializer = None

        rented = []
        if rentedHomeserializer is not None:
            rented.append(rentedHomeserializer.data)
        if rentedPlotserializer is not None:
            rented.append(rentedPlotserializer.data)
        if rentedCommercialserializer is not None:
            rented.append(rentedCommerical.data)

        try:
            saleHomes = HomeSaleModel.objects.get(agent=agent_id)
            saleHomeserializer = HomeSaleSerializer(saleHomes)
        except:
            saleHomeserializer = None

        try:
            salePlots = PlotSaleModel.objects.get(agent=agent_id)
            salePlotserializer = HomeSaleSerializer(salePlots)
        except:
            salePlotserializer = None

        try:
            saleCommerical = CommercialSaleModel.objects.get(agent=agent_id)
            saleCommericalserializer = HomeSaleSerializer(saleCommerical)
        except:
            saleCommericalserializer = None
        sale = []
        if saleHomeserializer is not None:
            sale.append(saleHomeserializer.data)
        if salePlotserializer is not None:
            sale.append(salePlotserializer.data)
        if saleCommericalserializer is not None:
            sale.append(saleCommericalserializer.data)

        if sale and rented:
            data = {
                "sale": sale,
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if sale and not rented:
            data = {
                "sale": sale
            }
            return Response(data, status=status.HTTP_200_OK)

        if rented and not sale:
            data = {
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if not sale and not rented:
            return Response({"msg": "Nothing is Listed"}, status=status.HTTP_200_OK)


class listAuthPropertiesViewset(viewsets.ModelViewSet):
    queryset = CommercialSaleModel.objects.all()
    serializer_class = CommercialSaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user_id = request.user.id
        agent_id = Agent.objects.get(user=user_id)

        try:
            rentedHomes = HomeRentModel.objects.get(agent=agent_id)
            rentedHomeserializer = HomeRentSerializer(rentedHomes)
        except:
            rentedHomeserializer = None

        try:
            rentedPlots = PlotRentModel.objects.get(agent=agent_id)
            rentedPlotserializer = HomeRentSerializer(rentedPlots)
        except:
            rentedPlotserializer = None

        try:
            rentedCommerical = CommercialRentModel.objects.get(agent=agent_id)
            rentedCommercialserializer = HomeRentSerializer(rentedCommerical)
        except:
            rentedCommercialserializer = None

        rented = []
        if rentedHomeserializer is not None:
            rented.append(rentedHomeserializer.data)
        if rentedPlotserializer is not None:
            rented.append(rentedPlotserializer.data)
        if rentedCommercialserializer is not None:
            rented.append(rentedCommercialserializer.data)

        try:
            saleHomes = HomeSaleModel.objects.get(agent=agent_id)
            saleHomeserializer = HomeSaleSerializer(saleHomes)
        except:
            saleHomeserializer = None

        try:
            salePlots = PlotSaleModel.objects.get(agent=agent_id)
            salePlotserializer = HomeSaleSerializer(salePlots)
        except:
            salePlotserializer = None

        try:
            saleCommerical = CommercialSaleModel.objects.get(agent=agent_id)
            saleCommericalserializer = HomeSaleSerializer(saleCommerical)
        except:
            saleCommericalserializer = None
        sale = []
        if saleHomeserializer is not None:
            sale.append(saleHomeserializer.data)
        if salePlotserializer is not None:
            sale.append(salePlotserializer.data)
        if saleCommericalserializer is not None:
            sale.append(saleCommericalserializer.data)

        if sale and rented:
            data = {
                "sale": sale,
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if sale and not rented:
            data = {
                "sale": sale
            }
            return Response(data, status=status.HTTP_200_OK)

        if rented and not sale:
            data = {
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if not sale and not rented:
            return Response({"msg": "Nothing is Listed"}, status=status.HTTP_200_OK)


class listAllPropertiesViewset(viewsets.ModelViewSet):
    queryset = CommercialSaleModel.objects.all()
    serializer_class = CommercialSaleSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        # import pdb;pdb.set_trace()
        try:
            rentedHomes = HomeRentModel.objects.all()
            rentedHomeserializer = HomeRentSerializer(rentedHomes, many=True)
        except:
            rentedHomeserializer = None

        try:
            rentedPlots = PlotRentModel.objects.all()
            rentedPlotserializer = HomeRentSerializer(rentedPlots, many=True)
        except:
            rentedPlotserializer = None

        try:
            rentedCommerical = CommercialRentModel.objects.all()
            rentedCommercialserializer = HomeRentSerializer(rentedCommerical, many=True)
        except:
            rentedCommercialserializer = None

        rented = []
        if rentedHomeserializer is not None:
            rented.append(rentedHomeserializer.data)
        if rentedPlotserializer is not None:
            rented.append(rentedPlotserializer.data)
        if rentedCommercialserializer is not None:
            rented.append(rentedCommercialserializer.data)

        try:
            saleHomes = HomeSaleModel.objects.all()
            saleHomeserializer = HomeSaleSerializer(saleHomes, many=True)
        except:
            saleHomeserializer = None

        try:
            salePlots = PlotSaleModel.objects.all()
            salePlotserializer = HomeSaleSerializer(salePlots, many=True)
        except:
            salePlotserializer = None

        try:
            saleCommerical = CommercialSaleModel.objects.all()
            saleCommericalserializer = HomeSaleSerializer(saleCommerical, many=True)
        except:
            saleCommericalserializer = None
        sale = []
        if saleHomeserializer is not None:
            sale.append(saleHomeserializer.data)
        if salePlotserializer is not None:
            sale.append(salePlotserializer.data)
        if saleCommericalserializer is not None:
            sale.append(saleCommericalserializer.data)

        if sale and rented:
            data = {
                "sale": sale,
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if sale and not rented:
            data = {
                "sale": sale
            }
            return Response(data, status=status.HTTP_200_OK)

        if rented and not sale:
            data = {
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if not sale and not rented:
            return Response({"msg": "Nothing is Listed"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def AgentsData(request, pk=None):
    if request.method == "GET":
        try:
            rentedHomes = HomeRentModel.objects.get(agent=pk)
            rentedHomeserializer = HomeRentSerializer(rentedHomes, many=True)
        except:
            rentedHomeserializer = None

        try:
            rentedPlots = PlotRentModel.objects.get(agent=pk)
            rentedPlotserializer = HomeRentSerializer(rentedPlots, many=True)
        except:
            rentedPlotserializer = None

        try:
            rentedCommerical = CommercialRentModel.get(agent=pk)
            rentedCommercialserializer = HomeRentSerializer(rentedCommerical, many=True)
        except:
            rentedCommercialserializer = None

        rented = []
        if rentedHomeserializer is not None:
            rented.append(rentedHomeserializer.data)
        if rentedPlotserializer is not None:
            rented.append(rentedPlotserializer.data)
        if rentedCommercialserializer is not None:
            rented.append(rentedCommercialserializer.data)

        try:
            saleHomes = HomeSaleModel.objects.all()
            saleHomeserializer = HomeSaleSerializer(saleHomes, many=True)
        except:
            saleHomeserializer = None

        try:
            salePlots = PlotSaleModel.objects.all()
            salePlotserializer = HomeSaleSerializer(salePlots, many=True)
        except:
            salePlotserializer = None

        try:
            saleCommerical = CommercialSaleModel.objects.all()
            saleCommericalserializer = HomeSaleSerializer(saleCommerical, many=True)
        except:
            saleCommericalserializer = None
        sale = []
        if saleHomeserializer is not None:
            sale.append(saleHomeserializer.data)
        if salePlotserializer is not None:
            sale.append(salePlotserializer.data)
        if saleCommericalserializer is not None:
            sale.append(saleCommericalserializer.data)

        if sale and rented:
            data = {
                "sale": sale,
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if sale and not rented:
            data = {
                "sale": sale
            }
            return Response(data, status=status.HTTP_200_OK)

        if rented and not sale:
            data = {
                "rent": rented
            }
            return Response(data, status=status.HTTP_200_OK)

        if not sale and not rented:
            return Response({"msg": "Nothing is Listed"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def SearchHomeRentProperties(self, request):
    if request.method == 'GET':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
