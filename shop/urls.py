from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProductViewsets

router = routers.DefaultRouter()
router.register('Products   ',ProductViewsets)

urlpatterns = [
    
    path('',include(router.urls)),
    path('tokenrequest/',obtain_auth_token),
]