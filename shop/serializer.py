from rest_framework import serializers
from .models import Product,Category,Rating,ProductComments


class ProductCommentsserializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComments
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_comments = ProductCommentsserializer(many=True)
    class Meta:
        model = Product
        fields = ['id','category','name','slug','image','discription','price','available','created','updated','nom_of_ratings','avg_rating','product_comments']
        