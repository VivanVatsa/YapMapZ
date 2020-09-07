import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map([38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

# used a for loop to iterative the data of the csv file into the python file to mark it on the web map and then display it in the form of marker.


# i can concatenate the elevation popup with metres and the elevation value
# for lt, ln, el in zip(lat, lon, elev):
#     fg.add_child(folium.Marker(
#         location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=color_producer(el))))

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(
        el) + " m", fill_color=color_producer(el), color='grey', fill_opacity=0.7))

# for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
#     map.add_child(folium.Marker(location=coordinates,
#                                 popup="heya im a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
