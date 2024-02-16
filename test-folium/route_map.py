import os
import webbrowser
import folium

# Creating a map centered at a specific location
mymap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Adding markers for the start and end points
start_point = [48.8566, 2.3522]
end_point = [48.8599, 2.3399]

# Adding markers for the start and end points
folium.Marker(location=start_point, popup="Starting Point").add_to(mymap)
folium.Marker(location=end_point, popup="End Point").add_to(mymap)

# Drawing a line between the start and end points
folium.PolyLine(locations=[start_point, end_point], color="blue").add_to(mymap)

# Saving the map to an HTML file
output_directory = "templates/"
output_filename = "route_map.html"
output_path = os.path.join(output_directory, output_filename)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

mymap.save(output_path)

# Opening the HTML file in the default web browser
webbrowser.open("file://" + os.path.abspath(output_path))
