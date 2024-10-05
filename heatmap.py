import json

import folium
import pandas as pd
from folium.plugins import HeatMap

# Read the CSV file into a pandas DataFrame
csv_file = "./gb_dataset.csv"  # Replace with your CSV file name
data = pd.read_csv(csv_file)

# Initialize the map centered around the United Kingdom
uk_center = [54.5, -3.4]  # Latitude and longitude roughly at the center of the UK


mymap = folium.Map(location=uk_center, zoom_start=6)

with open("./uk_polygon.geojson") as f:
    uk_geojson = json.load(f)

folium.GeoJson(
    uk_geojson,
    style_function=lambda feature: {
        "fillColor": "red",
        "color": "red",
        "fillOpacity": 0.2,  # Semi-transparent red overlay
        "weight": 0,  # No border around the polygon
    },
).add_to(mymap)


# Create a list of [latitude, longitude] pairs for the heatmap
heat_data = [[row["latitude"], row["longitude"]] for index, row in data.iterrows()]

# Add the HeatMap layer
HeatMap(
    heat_data, radius=15, blur=10, gradient={0.4: "navy", 0.65: "blue", 1: "lime"}
).add_to(mymap)

# Save the map to an HTML file
mymap.save("index.html")

print("Heatmap has been saved to heatmap_uk.html")
