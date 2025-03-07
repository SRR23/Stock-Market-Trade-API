import os
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import viewsets, pagination, status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from .models import TradeData
from .serializers import TradeDataSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Custom pagination class
class PaginationView(pagination.PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'

    def get_max_page_size(self, total_records):
        """Dynamically set max page size based on total records."""
        return max(50, total_records // 10)  # Ensures at least 50

    def paginate_queryset(self, queryset, request, view=None):
        total_records = len(queryset)  # Total data count
        self.max_page_size = self.get_max_page_size(total_records)  # Set max dynamically
        return super().paginate_queryset(queryset, request, view)


@api_view(['GET'])
def get_trade_data(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'stock_market_data.json')

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)  # Load full dataset

        # Get trade_code from query params
        trade_code = request.GET.get('trade_code')

        # Filter data if trade_code is provided
        if trade_code:
            data = [entry for entry in data if entry.get('trade_code') == trade_code]

        # Apply pagination
        paginator = PaginationView()
        paginated_data = paginator.paginate_queryset(data, request)

        return paginator.get_paginated_response(paginated_data)

    except FileNotFoundError:
        return JsonResponse({"error": "File not found"}, status=404)

# API to get unique trade codes (Paginated)
@api_view(['GET'])
def get_trade_codes(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'stock_market_data.json')

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Extract unique trade codes
        unique_trade_codes = list(set(entry["trade_code"] for entry in data))

        return JsonResponse({"trade_codes": unique_trade_codes}, safe=False)

    except FileNotFoundError:
        return JsonResponse({"error": "File not found"}, status=404)


# @api_view(['GET'])
# def get_trade_codes(request):
#     json_file_path = os.path.join(settings.BASE_DIR, 'stock_market_data.json')

#     try:
#         with open(json_file_path, 'r') as file:
#             data = json.load(file)

#         # Extract unique trade codes
#         unique_trade_codes = list(set(entry["trade_code"] for entry in data))

#         # Apply pagination to trade codes
#         paginator = PaginationView()
#         paginated_data = paginator.paginate_queryset(unique_trade_codes, request)

#         return paginator.get_paginated_response(paginated_data)

#     except FileNotFoundError:
#         return JsonResponse({"error": "File not found"}, status=404)
    

class TradeDataViewSet(viewsets.ModelViewSet):
    pagination_class = PaginationView  # Default pagination class
    serializer_class = TradeDataSerializer
    queryset = TradeData.objects.all()
    # Enable Django filtering and searching
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['trade_code']  # Allow searching by `trade_code`
    filterset_fields = ['trade_code']  # Allow filtering by `trade_code`


class UniqueTradeCodesView(APIView):
    def get(self, request):
        # Get unique trade codes from the database
        unique_trade_codes = TradeData.objects.values('trade_code').distinct()

        # Extract only the 'trade_code' field
        trade_codes = [entry['trade_code'] for entry in unique_trade_codes]

        return Response({'trade_codes': trade_codes}, status=status.HTTP_200_OK)
