import folium

# Create a map centered at a specific location
mymap = folium.Map(location=[-11.6642316, 27.4826264], zoom_start=12)

# Add a marker at a specific location
folium.Marker(location=[-11.6642316,27.4826264],popup='Lubumbashi').add_to(mymap)

# Save the map to an HTML file
mymap.save('my_map.html')