from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Rating,Category
from .serializer import ProductSerializer
# Create your views here.


class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer