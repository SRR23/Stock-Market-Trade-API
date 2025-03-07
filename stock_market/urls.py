from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TradeDataViewSet,
    get_trade_data,
    get_trade_codes,
    UniqueTradeCodesView,
)

router = DefaultRouter()
router.register(r"trades", TradeDataViewSet)  # CRUD API for SQL model

urlpatterns = [
    path("json-data/", get_trade_data, name="json-data"),  # JSON model API
    path("json-data/trade-code/", get_trade_codes, name="trade-code"),  # JSON model API
    path(
        "trades/trade-code/",
        UniqueTradeCodesView.as_view(),
        name="unique-trade-codes",
    ),
    path("", include(router.urls)),  # Include all routes from the router
]
