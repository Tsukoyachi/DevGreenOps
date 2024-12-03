import csv
import time
import paho.mqtt.client as mqtt
import os

# MQTT Configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "test/points"

# CSV File Path
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir,"generated_datasets","small_dataset.csv")

# MQTT Connection Callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker.")
    else:
        print(f"Failed to connect, return code {rc}")

# Initialize MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)

# Read CSV and Publish Data
def send_csv_data(csv_file, topic):
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert row to a string format (JSON-like)
            message = str(row)
            print(f"Publishing: {message} to topic: {topic}")
            client.publish(topic, message)
            time.sleep(1)  # Optional delay between messages

# Start the MQTT Client
client.loop_start()

try:
    send_csv_data(csv_file_path, TOPIC)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected from MQTT broker.")
