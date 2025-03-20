import pandas as pd

def calculate_routes(data, start_city, end_city):
    # Example logic: Print unique destinations and their counts
    destinations = data['Sold-To party city'].value_counts()
    if start_city not in destinations.index or end_city not in destinations.index:
        print("Invalid starting or ending city.")
        return

    print(f"Calculating route from {start_city} to {end_city}...")
    # Implement your algorithm here (e.g., Dijkstra's)

if __name__ == "__main__":
    data = pd.read_excel('normalized_dataset.xlsx')
    
    start_city = input("Enter starting city: ")
    end_city = input("Enter ending city: ")
    
    calculate_routes(data, start_city, end_city)
