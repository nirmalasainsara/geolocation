import requests
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from rest_framework import (
    status
)

from geolocation import settings

class GeoLocationApiView(APIView):
    """
    api view for geo location
    """
    
    def post(self, request, *args, **kwargs):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        token = settings.token
        address = self.request.GET
        
        data = requests.post(f'{url}?address={address}&key={token}')
        
        if data:
            return Response(data, status=status.HTTP_200_OK)

        return Response('data invalid', status=status.HTTP_400_BAD_REQUEST)
