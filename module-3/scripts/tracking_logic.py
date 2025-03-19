def track_shipment(gps_data):
    # Placeholder for shipment tracking logic
    print(f"Tracking shipment at location: {gps_data}")

if __name__ == "__main__":
    import gps_simulation  # Ensure you simulate GPS data first
    while True:
        gps_data = gps_simulation.generate_gps_data()
        track_shipment(gps_data)
        time.sleep(5)  # Adjust as needed
