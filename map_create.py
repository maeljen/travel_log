###Import of folium for map object manipulation and pandas for imported dataset handling
###Import of geopy/Nominatim to permit streamlining dataset to just locations
import folium
import pandas as pd
from geopy import Nominatim

# Read in pandas dataframes of past travels and future plans
# Consider building database backend for this so it can be updated/queried dynamically
past_data = pd.read_csv("visited.csv")
#future_data = pd.read_csv("planned.csv")

# Create geocoder object for location lookup within featuregroup loop
locator = Nominatim(user_agent="nomgeocoder")

# Generate list datatype objects for used fields from past & future data
# Headers for visited.csv are NAME, YEAR, MONTH, DURATION, TRIP, WITH, LAT, LON

past_namelist = list(past_data["NAME"])
past_yearlist = list(past_data["YEAR"])
past_monthlist = list(past_data["MONTH"])
past_durlist = list(past_data["DURATION"])
past_triplist = list(past_data["TRIP"])
#future_namelist = list(future_data["NAME"])
#future_latlist = list(future_data["LAT"])
#future_lonlist = list(future_data["LON"])

# Configure pop-up html
html = """<h4>Visited: %s</h4>
Trip: %s<br>
Year: %s<br>
Month: %s<br>
Duration: %s day/s
"""

# Create map object using folium
# Set starting location - Consider implementing start on current location
start_location = [40.481, -79.935]

map = folium.Map(location=start_location,zoom_start=3)

# Create feature group for each data-set to define
past_fg = folium.FeatureGroup(name="Matt's Past Travels")
#future_fg = folium.FeatureGroup(name="Matt's Future Plans")

# Iterate through data list to build feature group children
for place,trip,year,month,dur in zip(past_namelist,past_triplist,past_yearlist,past_monthlist,past_durlist):
    iframe = folium.IFrame(html=html % (str(place),str(trip),str(year),str(month),str(dur)),width=300,height=200)
    geoplace = locator.geocode(place)
    past_fg.add_child(folium.Marker(location=[geoplace.latitude,geoplace.longitude],popup=folium.Popup(iframe),icon=folium.Icon('green')))

#for lat,lon,place in zip(future_latlist,future_lonlist,future_namelist):
#   future_fg.add_child(folium).Marker(location=[lat,lon],popup=place,icon=folium.Icon('orange')))

map.add_child(past_fg)

# Enable layering - all FeatureGroups/Children should be added above this line
map.add_child(folium.LayerControl())

map.save("travel_log.html")