###Import of folium for map object manipulation and pandas for imported dataset handling
import folium
import pandas as pd

# Read in pandas dataframes of past travels and future plans
# Consider building database backend for this so it can be updated/queried dynamically
# Consider web lookup of lat/lon based on name to avoid having to hunt it down for well-known places
past_data = pd.read_csv("visited.csv")
#future_data = pd.read_csv("planned.csv")

# Generate list datatype objects for used fields from past & future data
# Headers for visited.csv are NAME, YEAR, MONTH, DURATION, TRIP, WITH, LAT, LON

past_namelist = list(past_data["NAME"])
past_latlist = list(past_data["LAT"])
past_lonlist = list(past_data["LON"])
#future_namelist = list(future_data["NAME"])
#future_latlist = list(future_data["LAT"])
#future_lonlist = list(future_data["LON"])



# Create map object using folium
# Set starting location - Consider implementing start on current location
start_location = [40.481, -79.935]

map = folium.Map(location=start_location,zoom_start=3)

# Create feature group for each data-set to define
past_fg = folium.FeatureGroup(name="Past Travels")
#future_fg = folium.FeatureGroup(name="Future Plans")

# Iterate through data list to build feature group children
for lat,lon,place in zip(past_latlist,past_lonlist,past_namelist):
    past_fg.add_child(folium.Marker(location=[lat,lon],popup=place,icon=folium.Icon('green')))

#for lat,lon,place in zip(future_latlist,future_lonlist,future_namelist):
#   future_fg.add_child(folium).Marker(location=[lat,lon],popup=place,icon=folium.Icon('orange')))

map.add_child(past_fg)

map.save("travel_log.html")


