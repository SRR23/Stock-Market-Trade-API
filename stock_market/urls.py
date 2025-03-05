from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TradeDataViewSet, 
    get_trade_data
)

router = DefaultRouter()
router.register(r'trades', TradeDataViewSet)  # CRUD API for SQL model

urlpatterns = [
    path('json-data/', get_trade_data, name='json-data'),  # JSON model API
    path('', include(router.urls)),  # Include all routes from the router
]
