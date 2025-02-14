from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BovinosView(APIView):
    def get(self, request):
        data = {
            "Módulo de Producción de Bovinos": "Esta es la primera petición a la API del módulo de producción de bovinos."
        }
        return Response(data, status=status.HTTP_200_OK)