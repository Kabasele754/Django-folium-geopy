from django.urls import path
from my_app.views.maps_view import AddressMapView, address_maps
from my_app.views.route_map import RouteMapView, route_map
from my_app.views.satellite_maps import SatelliteMapView, satellite_maps

urlpatterns = [
    # path('address-maps/', address_maps),
    path('address-maps/', AddressMapView.as_view()),
    # path('satellite-maps/', satellite_maps),
    path('satellite-maps/', SatelliteMapView.as_view()),
    # path('route_map/', route_map),
    path('route_map/', RouteMapView.as_view()),
]