from django.urls import path,include
from rest_framework import routers
from .views import CartViewSets

router = routers.DefaultRouter()
router.register('items',CartViewSets)


urlpatterns = [
    
    path('',include(router.urls)),
    
]
