import folium

def visualize_route(start_coords, end_coords):
    # Create a map centered at the midpoint between start and end
    m = folium.Map(location=[(start_coords[0] + end_coords[0]) / 2,
                              (start_coords[1] + end_coords[1]) / 2], zoom_start=10)

    # Add markers for start and end points
    folium.Marker(location=start_coords, popup='Start', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=end_coords, popup='End', icon=folium.Icon(color='red')).add_to(m)

    # Draw a line between the start and end points
    folium.PolyLine(locations=[start_coords, end_coords], color='blue').add_to(m)

    # Save the map to an HTML file
    m.save('route_map.html')
    print("Map has been saved as route_map.html")

if __name__ == "__main__":
    # Example coordinates (latitude, longitude)
    start_coordinates = (37.7749, -122.4194)  # San Francisco
    end_coordinates = (34.0522, -118.2437)    # Los Angeles
    
    visualize_route(start_coordinates, end_coordinates)
