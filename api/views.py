from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import FundoImobiliarioSerializer
from rest_framework import viewsets, permissions
from api.models import FundoImobiliario


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
  queryset = FundoImobiliario.objects.all()
  serializer_class = FundoImobiliarioSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['codigo', 'setor']