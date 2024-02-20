from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Rating,Category,ProductComments
from .serializer import ProductSerializer,ProductCommentsserializer,ProductRateingializer
# Create your views here.




class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCommentsViewsets(viewsets.ModelViewSet):
    queryset = ProductComments.objects.all()
    serializer_class = ProductCommentsserializer

class ProductRateingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = ProductRateingializer


