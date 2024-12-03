import influxdb_client, os, time
import csv
from influxdb_client import Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch InfluxDB connection parameters
token = os.getenv("INFLUX_TOKEN")
org = "Polytech"
url = "http://localhost:8086"

# Initialize the InfluxDB client
write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

# Path to your CSV dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "generated_datasets", "medium_dataset.csv")

try:
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row
        next(csv_reader)
        
        # Loop through the data and insert into InfluxDB
        for row in csv_reader:
            try:
                x = float(row[0])  # x value
                y = float(row[1])  # y value
                
                # Create a point for the database
                point = Point("points") \
                    .tag("device", "sensor1") \
                    .field("x", x) \
                    .field("y", y) 

                # Write to InfluxDB
                write_api.write(bucket="points", org=org, record=point)
                #print(f"Inserted point (x={x}, y={y})")
            except ValueError as e:
                print(f"Error processing row {row}: {e}")

except FileNotFoundError as e:
    print(f"Error: File not found at {csv_file_path}: {e}")

# Close the InfluxDB client after writing data
write_client.close()

print("Data insertion complete.")
