import folium

map = folium.Map([38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[
              38.2, -99.1], popup="heya im a marker", icon=folium.Icon(color='green')))
map.save("Map1.html")
