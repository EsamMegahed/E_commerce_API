from django.shortcuts import render
from rest_framework import viewsets
from .models import Cart
from .serializer import CartSerializers
# Create your views here.


class CartViewSets(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers