# tracking_logic.py
import os
import random
import time
import pandas as pd

# ------------------------------
# Geofence Configuration
# ------------------------------
geofence_boundary = {
    "min_latitude": 34.0,
    "max_latitude": 38.0,
    "min_longitude": -120.0,
    "max_longitude": -118.0,
}

# ------------------------------
# GPS Logging Configuration
# ------------------------------
GPS_LOG_FILE = r"E:\LMS\Logistic-Management-System\module-3\data\gps_log.csv"  # Save logs in the data directory

# ------------------------------
# Core Functions
# ------------------------------
def fetch_real_gps_data():
    """Simulate real GPS data (replace with API calls later)."""
    return {
        "latitude": round(random.uniform(-90, 90), 6),
        "longitude": round(random.uniform(-180, 180), 6),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def is_inside_geofence(gps_data):
    """Check if GPS coordinates are inside the geofence."""
    return (
        geofence_boundary["min_latitude"] <= gps_data["latitude"] <= geofence_boundary["max_latitude"]
        and geofence_boundary["min_longitude"] <= gps_data["longitude"] <= geofence_boundary["max_longitude"]
    )

def log_gps_data(gps_data):
    """Log GPS data to a CSV file."""
    try:
        # Load existing data or create a new DataFrame
        df = pd.read_csv(GPS_LOG_FILE) if pd.io.common.file_exists(GPS_LOG_FILE) else pd.DataFrame()
        
        # Append new data
        df = pd.concat([df, pd.DataFrame([gps_data])], ignore_index=True)
        df.to_csv(GPS_LOG_FILE, index=False)
    except Exception as e:
        print(f"Error logging GPS data: {e}")

def track_shipment(gps_data):
    """Track shipment and trigger alerts based on geofence."""
    if is_inside_geofence(gps_data):
        status = "INSIDE GEOFENCE"
    else:
        status = "OUTSIDE GEOFENCE"
    
    print(f"[{gps_data['timestamp']}] Location: {gps_data['latitude']}, {gps_data['longitude']} | Status: {status}")

# ------------------------------
# Main Execution Loop
# ------------------------------
if __name__ == "__main__":
    try:
        while True:
            gps_data = fetch_real_gps_data()  # Fetch GPS data
            track_shipment(gps_data)          # Track with geofence checks
            log_gps_data(gps_data)            # Log data to CSV
            time.sleep(5)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        print("\nTracking stopped by user.")

