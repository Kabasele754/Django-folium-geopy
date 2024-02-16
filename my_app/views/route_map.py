from django.http import HttpResponse
from django.shortcuts import render
import folium
from django.views import View
from geopy.geocoders import Nominatim


# define route maps class
class RouteMapView(View):
    template_name = 'myapp/route_map.html'
    context = {}

    def get(self, *args, **kwargs):

        # Creating a default Folium map
        default_map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
        default_map_html = default_map._repr_html_()

        # Passing default map data to the template context
        self.context['map_html'] = default_map_html

        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            start_address = self.request.POST.get('start_address')
            end_address = self.request.POST.get('end_address')

            # Geocode start and end addresses to get coordinates
            geolocator = Nominatim(user_agent="myapp")
            start_location = geolocator.geocode(start_address)
            end_location = geolocator.geocode(end_address)

            if start_location and end_location:
                start_point = [start_location.latitude, start_location.longitude]
                end_point = [end_location.latitude, end_location.longitude]

                # Creating a map centered at the start location
                my_map = folium.Map(location=start_point, zoom_start=12)

                # Adding markers for the start and end points
                folium.Marker(location=start_point, popup=start_location.address).add_to(my_map)
                folium.Marker(location=end_point, popup=end_location.address).add_to(my_map)

                # Drawing a line between the start and end points
                folium.PolyLine(locations=[start_point, end_point], color="blue").add_to(my_map)

                # Get the HTML representation of the map
                map_html = my_map._repr_html_()

                # Return the HTML content as a response
                return HttpResponse(map_html)
            else:
                return HttpResponse("Invalid addresses")

        return render(self.request, self.template_name)


#  the function route maps
def route_map(request):
    if request.method == 'POST':
        start_address = request.POST.get('start_address')
        end_address = request.POST.get('end_address')

        # Geocode start and end addresses to get coordinates
        geolocator = Nominatim(user_agent="myapp")
        start_location = geolocator.geocode(start_address)
        end_location = geolocator.geocode(end_address)

        if start_location and end_location:
            start_point = [start_location.latitude, start_location.longitude]
            end_point = [end_location.latitude, end_location.longitude]

            # Creating a map centered at the start location
            my_map = folium.Map(location=start_point, zoom_start=12)

            # Adding markers for the start and end points
            folium.Marker(location=start_point, popup=start_location.address).add_to(my_map)
            folium.Marker(location=end_point, popup=end_location.address).add_to(my_map)

            # Drawing a line between the start and end points
            folium.PolyLine(locations=[start_point, end_point], color="blue").add_to(my_map)

            # Get the HTML representation of the map
            map_html = my_map._repr_html_()

            # Return the HTML content as a response
            return HttpResponse(map_html)
        else:
            return HttpResponse("Invalid addresses")

    return render(request, 'myapp/route_map.html')



