import folium

# Creating a map centered at a specific location
mymap = folium.Map(location=[-11.6642316, 27.4826264], zoom_start=12)

# Adding a circle with a radius of 1000 meters (1 kilometer)

folium.Circle(
    location=[-11.6642316, 27.4826264],
    radius=1000,  # Radius in meters
    color="red",  # Circle border color
    fill=True,    # Fill the circle
    fill_color="red",  # Fill color
    fill_opacity=0.2,  # Opacity of the fill
).add_to(mymap)

# Save the map to an HTML file
mymap.save("circle_map.html")