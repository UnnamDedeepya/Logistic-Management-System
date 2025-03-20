import folium
import pandas as pd

# Sample dataset for cities and their coordinates
data = {
    "City": ["San Francisco", "Los Angeles", "Las Vegas", "Phoenix"],
    "Latitude": [37.7749, 34.0522, 36.1699, 33.4484],
    "Longitude": [-122.4194, -118.2437, -115.1398, -112.0740]
}
cities_df = pd.DataFrame(data)

def calculate_route(start_city, end_city):
    # Find coordinates for the start and end cities
    start_coords = cities_df[cities_df["City"] == start_city][["Latitude", "Longitude"]].values[0]
    end_coords = cities_df[cities_df["City"] == end_city][["Latitude", "Longitude"]].values[0]
    
    return start_coords, end_coords

def visualize_route(start_coords, end_coords):
    # Create a map centered at the midpoint between start and end
    m = folium.Map(location=[(start_coords[0] + end_coords[0]) / 2,
                             (start_coords[1] + end_coords[1]) / 2], zoom_start=6)

    # Add markers for start and end points
    folium.Marker(location=start_coords.tolist(), popup='Start', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=end_coords.tolist(), popup='End', icon=folium.Icon(color='red')).add_to(m)

    # Draw a line between the start and end points
    folium.PolyLine(locations=[start_coords.tolist(), end_coords.tolist()], color='blue').add_to(m)

    # Save the map to an HTML file
    m.save('route_map.html')
    print("Map has been saved as route_map.html")

if __name__ == "__main__":
    # Get user input for starting and ending cities
    print("Available cities:", ", ".join(cities_df["City"]))
    start_city = input("Enter starting city: ")
    end_city = input("Enter ending city: ")

    if start_city not in cities_df["City"].values or end_city not in cities_df["City"].values:
        print("Invalid city names. Please choose from the available cities.")
    else:
        # Calculate route based on user input
        start_coords, end_coords = calculate_route(start_city, end_city)
        
        # Visualize the route on a map
        visualize_route(start_coords, end_coords)
