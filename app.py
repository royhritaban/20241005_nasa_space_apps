import folium
import pandas as pd

# Read the CSV file into a pandas DataFrame
csv_file = "./human_refined_data_uk.csv"  # Replace with your CSV file name
data = pd.read_csv(csv_file)

# Initialize the map centered around the United Kingdom
uk_center = [54.5, -3.4]  # Latitude and longitude roughly at the center of the UK
mymap = folium.Map(location=uk_center, zoom_start=6)


# Function to convert miles to kilometers (for folium)
def miles_to_km(miles):
    return miles * 1.60934


# Loop through the CSV data and add markers
for index, row in data.iterrows():
    # Extract latitude and longitude
    latitude = row["latitude"]
    longitude = row["longitude"]

    # Create a marker for each location
    # folium.Marker(
    #     location=[latitude, longitude],
    #     popup=f"Title: {row['title']}<br>Category: {row['category']}<br>Address: {row['complete_address']}",
    #     icon=folium.Icon(color="blue", icon="info-sign"),
    # ).add_to(mymap)

    # Add a circle with a 3-mile radius (4.83 km)
    folium.Circle(
        radius=miles_to_km(3) * 1000,  # Convert miles to meters
        location=[latitude, longitude],
        color="red",
        fill=True,
        fill_opacity=0.2,
    ).add_to(mymap)

# Save the map to an HTML file
mymap.save("map_uk_markers.html")

print("Map has been saved to map_uk_markers.html")
