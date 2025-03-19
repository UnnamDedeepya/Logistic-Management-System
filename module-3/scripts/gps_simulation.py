import random
import time

def generate_gps_data():
    return {
        "latitude": round(random.uniform(-90, 90), 6),
        "longitude": round(random.uniform(-180, 180), 6)
    }

# Simulate GPS data every few seconds
while True:
    gps_data = generate_gps_data()
    print("Simulated GPS Data:", gps_data)
    time.sleep(5)  # Adjust the sleep time as needed
