import folium

map = folium.Map([38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    map.add_child(folium.Marker(location=coordinates,
                                popup="heya im a marker", icon=folium.Icon(color='green')))

# map.add_child(folium.Marker(location=[37.2, -97.1], popup="heya im a marker 2", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
