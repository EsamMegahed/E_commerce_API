from django.contrib import admin
from .models import Category,Product,Rating,ProductComments
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(ProductComments)