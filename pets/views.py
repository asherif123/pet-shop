from rest_framework import permissions, viewsets, mixins
from pets.models import Pet, Order
from pets.serializers import PetSerializer, OrderSerializer



class PetViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for Pets CRUD API.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.AllowAny]


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A ViewSet for creating pets orders API.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
