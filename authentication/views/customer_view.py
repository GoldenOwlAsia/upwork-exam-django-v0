from authentication.models import Customer
from authentication.serializers import CustomerSerializer
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
