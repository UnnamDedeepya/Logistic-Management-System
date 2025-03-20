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
    start_lat = float(input("Enter starting latitude: "))
    start_lon = float(input("Enter starting longitude: "))
    end_lat = float(input("Enter ending latitude: "))
    end_lon = float(input("Enter ending longitude: "))

    visualize_route((start_lat, start_lon), (end_lat, end_lon))
