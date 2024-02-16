from django.shortcuts import render
import folium
from django.views import View
from geopy.geocoders import Nominatim


# define Address Maps class
class AddressMapView(View):
    template_name = 'myapp/search_map.html'
    context = {}

    def get(self, *args, **kwargs):

        # Creating a default Folium map
        default_map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
        default_map_html = default_map._repr_html_()

        # Passing default map data to the template context
        self.context['map_html'] = default_map_html

        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        # If the request method is POST, process the form submission
        if self.request.method == 'POST':
            address = self.request.POST.get('address')
            print("see address", address)
            # Geocoding the address
            geolocator = Nominatim(user_agent="myapp")
            location = geolocator.geocode(address)
            if location:
                print(location)
                # Creating the Folium map with user-entered address location
                my_map = folium.Map(location=[location.latitude, location.longitude], zoom_start=16)
                folium.Marker(location=[location.latitude, location.longitude], popup=address).add_to(my_map)
                # Customizing marker icon to a home icon
                folium.Marker(location=[location.latitude, location.longitude], popup=address,
                              icon=folium.Icon(color="blue", icon="home"), ).add_to(my_map)
                # Customizing popup with HTML content
                country = location.address.split(', ')[-1]
                print("Pays:", country)
                html_popup = f"<b>{country}</b><br><i>{location.address}</i>"
                folium.Marker(
                    location=[location.latitude, location.longitude], popup=folium.Popup(html_popup, max_width=300)
                ).add_to(my_map)

                # Adding a circle with a radius of 1000 meters (1 kilometer)
                folium.Circle(location=[location.latitude, location.longitude], radius=50, color="red", fill=True,
                              fill_color="red", fill_opacity=0.2, ).add_to(my_map)

                # Rendering the map into HTML representation
                map_html = my_map._repr_html_()

                # Passing the map data to the template context
                self.context['map_html'] = map_html
        return render(self.request, self.template_name, self.context)


# define the function address maps
def address_maps(request):
    context = {}

    # Creating a default Folium map
    default_map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    default_map_html = default_map._repr_html_()

    # Passing default map data to the template context
    context['map_html'] = default_map_html

    # If the request method is POST, process the form submission
    if request.method == 'POST':
        address = request.POST.get('address')
        print("see address", address)

        # Geocoding the address
        geolocator = Nominatim(user_agent="myapp")
        location = geolocator.geocode(address)
        if location:
            print(location)

            # Creating the Folium map with user-entered address location
            my_map = folium.Map(location=[location.latitude, location.longitude], zoom_start=16)
            folium.Marker(location=[location.latitude, location.longitude], popup=address).add_to(my_map)
            # Customizing marker icon to a home icon
            folium.Marker( location=[location.latitude, location.longitude], popup=address,
                           icon=folium.Icon(color="blue", icon="home"),).add_to(my_map)

            # Customizing popup with HTML content
            country = location.address.split(', ')[-1]
            print("Pays:", country)
            html_popup = f"<b>{country}</b><br><i>{location.address}</i>"
            folium.Marker(
                location=[location.latitude, location.longitude], popup=folium.Popup(html_popup, max_width=300)
            ).add_to(my_map)

            # Adding a circle with a radius of 1000 meters (1 kilometer)
            folium.Circle(location=[location.latitude, location.longitude], radius=50, color="red", fill=True,
                          fill_color="red", fill_opacity=0.2, ).add_to(my_map)

            # Rendering the map into HTML representation
            map_html = my_map._repr_html_()

            # Passing the map data to the template context
            context['map_html'] = map_html

    return render(request, 'myapp/search_map.html', context)



