import random
import time

def fetch_real_gps_data():
    # Simulate fetching real GPS data (replace with actual API call)
    return {
        "latitude": round(random.uniform(-90, 90), 6),
        "longitude": round(random.uniform(-180, 180), 6)
    }

def track_shipment(gps_data):
    print(f"Tracking shipment at location: Latitude {gps_data['latitude']}, Longitude {gps_data['longitude']}")

if __name__ == "__main__":
    while True:
        gps_data = fetch_real_gps_data()
        track_shipment(gps_data)
        time.sleep(5)  # Adjust the sleep time as needed
