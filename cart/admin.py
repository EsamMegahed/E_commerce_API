from django.contrib import admin
from .models import CartItems,Order
# Register your models here.

admin.site.register(CartItems)
admin.site.register(Order)