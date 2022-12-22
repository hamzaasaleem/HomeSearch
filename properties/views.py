from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from accounts.serializers import AgentProfileSerializer
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView


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
            rentedHomes = HomeRentModel.objects.filter(agent=pk)
            rentedHomeserializer = HomeRentSerializer(rentedHomes, many=True)
        except:
            rentedHomeserializer = None

        try:
            rentedPlots = PlotRentModel.objects.filter(agent=pk)
            rentedPlotserializer = HomeRentSerializer(rentedPlots, many=True)
        except:
            rentedPlotserializer = None

        try:
            rentedCommerical = CommercialRentModel.filter(agent=pk)
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
            saleHomes = HomeSaleModel.objects.filter(agent=pk)
            saleHomeserializer = HomeSaleSerializer(saleHomes, many=True)
        except:
            saleHomeserializer = None

        try:
            salePlots = PlotSaleModel.objects.filter(agent=pk)
            salePlotserializer = HomeSaleSerializer(salePlots, many=True)
        except:
            salePlotserializer = None

        try:
            saleCommerical = CommercialSaleModel.objects.filter(agent=pk)
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


class PropertyHomeRentFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    advance_rent = filters.NumberFilter(field_name="advance_rent", lookup_expr='lte')
    monthly_rent = filters.NumberFilter(field_name="monthly_rent", lookup_expr='lte')

    class Meta:
        model = HomeRentModel
        fields = ['monthly_rent', 'advance_rent', 'city', 'address', 'area', 'bedrooms', 'bathrooms']


class PropertyHomeRentList(ListAPIView):
    queryset = HomeRentModel.objects.all()
    serializer_class = HomeRentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['monthly_rent', 'advance_rent', 'city', 'address', 'area', 'bedrooms', 'bathrooms']



class PropertyPlotRentFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    advance_rent = filters.NumberFilter(field_name="advance_rent", lookup_expr='lte')
    monthly_rent = filters.NumberFilter(field_name="monthly_rent", lookup_expr='lte')

    class Meta:
        model = PlotRentModel
        fields = ['monthly_rent', 'advance_rent', 'city', 'address', 'area']


class PropertyPlotRentList(ListAPIView):
    queryset = PlotRentModel.objects.all()
    serializer_class = PlotRentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =  ['monthly_rent', 'advance_rent', 'city', 'address', 'area']




class PropertyCommercialRentFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    advance_rent = filters.NumberFilter(field_name="advance_rent", lookup_expr='lte')
    monthly_rent = filters.NumberFilter(field_name="monthly_rent", lookup_expr='lte')

    class Meta:
        model = CommercialRentModel
        fields = ['monthly_rent', 'advance_rent', 'city', 'address', 'area']


class PropertyCommercialRentList(ListAPIView):
    queryset = PlotRentModel.objects.all()
    serializer_class = PlotRentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =  ['monthly_rent', 'advance_rent', 'city', 'address', 'area']



class PropertyHomeSaleFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = HomeSaleModel
        fields = ['price', 'installment', 'city', 'address', 'area', 'bedrooms', 'bathrooms']


class PropertyHomeSaleList(ListAPIView):
    queryset = HomeSaleModel.objects.all()
    serializer_class = HomeSaleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'installment', 'city', 'address', 'area', 'bedrooms', 'bathrooms']


class PropertyPlotSaleFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = PlotSaleModel
        fields = ['price', 'installment', 'city', 'address', 'area']


class PropertyPlotSaleList(ListAPIView):
    queryset = PlotSaleModel.objects.all()
    serializer_class = PlotSaleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'installment', 'city', 'address', 'area']




class PropertyCommercialSaleFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')


    class Meta:
        model = CommercialSaleModel
        fields = ['price', 'installment', 'city', 'address', 'area']


class PropertyCommercialSaleList(ListAPIView):
    queryset = CommercialSaleModel.objects.all()
    serializer_class = CommercialSaleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'installment', 'city', 'address', 'area']