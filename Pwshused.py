import folium

# map = folium.Map(location=[89, -99])
# map
# folium.folium.Map object at 0x092F9520 >
map.save("Map1.html")
map = folium.Map(location=[55.33, -12.44])
map.save("Map1.html")
map = folium.Map(location=[22.26, 73.184])
map.save("Map1.html")
# map = folium.Map(location=[55.33, -12.44], zoom_start)
# File "<stdin>", line 1
# SyntaxError: positional argument follows keyword argument
map = folium.Map(location=[55.33, -12.44], zoom_start=6)
map.save("Map1.html")
