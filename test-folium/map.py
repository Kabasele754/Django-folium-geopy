import os
import webbrowser
import folium

# Creating a map centered at a specific location
mymap = folium.Map(location=[48.8566, 2.3522], zoom_start=16)

# Advanced Customization: Adding a marker with customizations
# You can adjust colors, icons, popups, and other parameters to meet specific needs.
# Customizing marker color to green
folium.Marker(
    location=[48.8566, 2.3522], popup="Paris", icon=folium.Icon(color="green")
).add_to(mymap)

# Customizing marker icon to a home icon
folium.Marker(
    location=[48.8566, 2.3522],
    popup="Paris",
    icon=folium.Icon(color="blue", icon="home"),
).add_to(mymap)

# Customizing popup with HTML content
html_popup = "<b>Paris</b><br><i>City of Lights</i>"
folium.Marker(
    location=[48.8566, 2.3522], popup=folium.Popup(html_popup, max_width=300)
).add_to(mymap)

# Adding a circle with a radius of 1000 meters (1 kilometer)
folium.Circle(
    location=[48.8566, 2.3522],
    radius=50,
    color="red",
    fill=True,
    fill_color="red",
    fill_opacity=0.2,
).add_to(mymap)

# Saving the map to an HTML file
output_directory = "test-folium/templates/"
output_filename = "my_map.html"
output_path = os.path.join(output_directory, output_filename)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

mymap.save(output_path)

# Opening the HTML file in the default web browser
absolute_path = os.path.abspath(output_path)
webbrowser.open("file://" + absolute_path)
