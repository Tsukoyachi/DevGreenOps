import json, os

def cleanWeatherJson(jsonObject):
    globalTagToRemove = ["queryCost", "tzoffset","stations"]
    dayTagToRemove = [
        "stations", 
        "source", 
        "datetimeEpoch", 
        "dew", 
        "solarradiation", 
        "solarenergy", 
        "sunriseEpoch", 
        "sunsetEpoch",
        "precip",
        "precipprob",
        "preciptype",
        "precipcover",
        "visibility",
        "uvindex",
        "severerisk",
        "sunrise",
        "sunset",
        "moonphase",
        "description",
        "icon",
        "conditions",
        "snow",
        "snowdepth",
        "wind",
        "windgust",
        "winddir",
        "windspeed",
        "pressure",
        "cloudcover",
        "humidity",
        "visibility"
    ]
    
    # Remove the global tags from the root of the JSON object
    for tag in globalTagToRemove:
        if tag in jsonObject:
            del jsonObject[tag]
    
    # Check if the 'days' key exists in the root, and process the array if it does
    if "days" in jsonObject:
        for day in jsonObject["days"]:
            # Remove the tags from each day in the 'days' array
            for tag in dayTagToRemove:
                if tag in day:
                    del day[tag]
    
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_dir = os.path.join(current_dir, 'json')
    
    input_file = os.path.join(json_dir,"weather-input.json")
    output_file = os.path.join(json_dir,"weather-clean.json")
    
    data = None
    with open(input_file, 'r') as file:
        data = json.load(file)
        cleanWeatherJson(data)
    
    if (data != None):
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
