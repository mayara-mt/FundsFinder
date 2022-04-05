from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.serializers import FundoImobiliarioSerializer
from rest_framework import viewsets, permissions
from api.models import FundoImobiliario


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
  queryset = FundoImobiliario.objects.all()
  serializer_class = FundoImobiliarioSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ['codigo', 'setor']
  search_fields = ['codigo', 'setor']
  ordering_fields = [
    'dividend_yield_medio_12m',
    'setor',
    'vacancia_financeira',
    'vacancia_fisica',
    'quantidade_ativos']