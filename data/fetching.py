import urllib.request
import sys
import json
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('APIKEY')
city = "<YOUR-CITY-HERE>"

# Ensure the target directory exists
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, 'json')
os.makedirs(output_dir, exist_ok=True)

try:
    # Fetch the data
    ResultBytes = urllib.request.urlopen(
        f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/2023-11-30/2024-12-10?unitGroup=us&include=days&key={APIKEY}&contentType=json'
    )
    
    # Parse the results as JSON
    jsonData = json.load(ResultBytes)
    
    # Save JSON data to file
    output_file = os.path.join(output_dir, f'weather-input.json')
    with open(output_file, 'w') as json_file:
        json.dump(jsonData, json_file, indent=4)
    
    print(f"Weather data saved to {output_file}")

except urllib.error.HTTPError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
except urllib.error.URLError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
