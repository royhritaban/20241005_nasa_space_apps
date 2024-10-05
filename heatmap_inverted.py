import folium
import pandas as pd
from folium.plugins import HeatMap

# Read the CSV file into a pandas DataFrame
csv_file = "./gb_dataset.csv"  # Replace with your CSV file name
data = pd.read_csv(csv_file)

# Initialize the map centered around the United Kingdom
uk_center = [54.5, -3.4]  # Latitude and longitude roughly at the center of the UK
mymap = folium.Map(location=uk_center, zoom_start=6)


# Convert miles to kilometers for the radius
def miles_to_km(miles):
    return miles * 1.60934


# Create a list of [latitude, longitude, weight] for the heatmap with a radius of 3 miles (4.83 km)
heat_data = [[row["latitude"], row["longitude"], 1] for index, row in data.iterrows()]

# Custom gradient for inversion: Red for low density, Green for high density
gradient = {
    0.4: "green",  # Most covered places (high density)
    0.65: "yellow",  # Medium density
    1.0: "red",  # Least covered places (low density)
}

# Add the inverted HeatMap layer
HeatMap(
    heat_data,
    radius=miles_to_km(3) * 10,  # 3-mile radius converted to kilometers and scaled
    blur=20,  # Smooth the heatmap further for a more even gradient
    gradient=gradient,  # Apply custom gradient
    min_opacity=0.2,
).add_to(mymap)

# Save the map to an HTML file
mymap.save("inverted_heatmap_uk.html")

print("Inverted heatmap has been saved to inverted_heatmap_uk.html")
