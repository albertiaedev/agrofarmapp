from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AvesView(APIView):
    def get(self, request):
        data = {
            "Módulo de Producción de Aves": "Esta es la primera petición a la API del módulo de producción de aves."
        }
        return Response(data, status=status.HTTP_200_OK)