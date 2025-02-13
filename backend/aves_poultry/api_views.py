from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PoultryListView(APIView):
    def get(self, request):
        data = {
            "Poultry": "First API request from the poultry module."
        }
        return Response(data, status=status.HTTP_200_OK)