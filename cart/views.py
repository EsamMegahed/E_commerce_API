from django.shortcuts import render
from rest_framework import viewsets
from .models import CartItems
from .serializer import CartSerializers
# Create your views here.


class CartViewSets(viewsets.ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartSerializers