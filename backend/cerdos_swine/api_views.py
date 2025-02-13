from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SwineListView(APIView):
    def get(self, request):
        data = {
            "Swine": "First API request from the swine module."
        }
        return Response(data, status=status.HTTP_200_OK)