import os  # Importing the os module for operating system related functions
import webbrowser  # Importing the webbrowser module for opening URLs in web browsers
import folium  # Importing the Folium library for creating interactive maps

# Creating a map centered at a specific location
mymap = folium.Map(location=[48.8566, 2.3522], zoom_start=17)

# Adding satellite map tiles with attribution
folium.TileLayer(
    tiles="https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
    attr="Google Satellite",
    name="Google Satellite",
    max_zoom=20,
    subdomains=["mt0", "mt1", "mt2", "mt3"],
).add_to(mymap)

# Adding a layer control to switch between map tiles
folium.LayerControl().add_to(mymap)

# Saving the map to an HTML file
output_directory = (
    "templates/"  # Define the output directory where the HTML file will be saved
)
output_filename = "satellite_map.html"  # Define the name of the HTML file
output_path = os.path.join(
    output_directory, output_filename
)  # Construct the full path to the HTML file

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

mymap.save(output_path)  # Save the map to the HTML file

# Opening the HTML file in the default web browser
webbrowser.open(
    "file://" + os.path.abspath(output_path)
)  # Open the HTML file in the default web browser
