import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# layering of the different components in map
# basically more like web map analyser.
# used are polygon layer
# pointer / marker layer


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map([38.58, -99.09], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

# used a for loop to iterative the data of the csv file into the python file to mark it on the web map and then display it in the form of marker.


# i can concatenate the elevation popup with metres and the elevation value
# for lt, ln, el in zip(lat, lon, elev):
#     fg.add_child(folium.Marker(
#         location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=color_producer(el))))

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(
        el) + " m", fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
# will use lambda function in the style_function parameter
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
# designed a classification algorithm for distinguishd population on the map

# for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
#     map.add_child(folium.Marker(location=coordinates,
#                                 popup="heya im a marker", icon=folium.Icon(color='green')))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")
