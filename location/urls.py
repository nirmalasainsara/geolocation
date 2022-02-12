from django.urls import re_path
from location.views import GeoLocationApiView


urlpatterns = [
    re_path(r'^getAddressDetails$', GeoLocationApiView.as_view(), name='getAddressDetails'),
]