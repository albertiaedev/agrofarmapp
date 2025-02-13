from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CattleListView(APIView):
    def get(self, request):
        data = {
            "Cattle": "First API request from the cattle module."
        }
        return Response(data, status=status.HTTP_200_OK)