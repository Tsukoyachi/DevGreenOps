import csv
import requests
import os

# Define the URL of the server endpoint
url = 'http://localhost:5000/upload'

# CSV File Path
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir,"generated_datasets","small_dataset.csv")

# Open the CSV file for reading
with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # You can customize the payload format depending on the CSV structure
        # For this example, let's assume each row contains a single value to send in the request body
        payload = {'data': row}
        
        # Send the POST request
        response = requests.post(url, json=payload)
        
        # Print the response from the server
        print(f"Response from server for row {row}: {response.text}")
