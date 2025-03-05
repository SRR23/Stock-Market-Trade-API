import os
import json
from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets
from .models import TradeData
from .serializers import TradeDataSerializer


# def get_trade_data(request):
#     with open('stock_market_data.json', 'r') as file:
#         data = json.load(file)
#     return JsonResponse(data, safe=False)

def get_trade_data(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'stock_market_data.json')  # Get absolute path
    
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        return JsonResponse({"error": "File not found"}, status=404)


class TradeDataViewSet(viewsets.ModelViewSet):
    queryset = TradeData.objects.all()
    serializer_class = TradeDataSerializer
