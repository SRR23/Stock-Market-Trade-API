
import json
from django.http import JsonResponse
from rest_framework import viewsets
from .models import TradeData
from .serializers import TradeDataSerializer


def get_trade_data(request):
    with open('stock_market_data.json', 'r') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)


class TradeDataViewSet(viewsets.ModelViewSet):
    queryset = TradeData.objects.all()
    serializer_class = TradeDataSerializer
