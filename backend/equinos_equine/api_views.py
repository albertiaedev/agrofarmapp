from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EquineListView(APIView):
    def get(self, request):
        data = {
            "Equine": "First API request from the equine module."
        }
        return Response(data, status=status.HTTP_200_OK)