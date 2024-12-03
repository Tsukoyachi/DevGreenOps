import os, json
from datetime import datetime
from random import sample
from copy import deepcopy

def meanOverList(jsonList, fieldName):
    values = [element[fieldName] for element in jsonList if fieldName in element]
    return round(sum(values) / len(values), 2) if values else 0

def computeMeanOverJson(jsonObject):
    if "days" not in jsonObject:
        return

    elementsToCompute = [
        "tempmin",
        "tempmax",
        "temp",
        "feelslikemin",
        "feelslikemax",
        "feelslike"
    ]
    
    means = {key: meanOverList(jsonObject["days"], key) for key in elementsToCompute}

    days = jsonObject.pop("days")
    jsonObject.update(means)
    jsonObject["days"] = days

def randomSamplingOverJson(jsonObject, percentageToKeep):
    if "days" not in jsonObject or percentageToKeep < 0 :
        return

    jsonResult = deepcopy(jsonObject)

    daysLength = len(jsonResult["days"])
    numToKeep = int(daysLength * (percentageToKeep / 100))
    
    print(f"Number of element : {daysLength}\n Number of element to keep : {numToKeep}")

    jsonResult["days"] = sample(jsonResult["days"], numToKeep)

    return jsonResult

def weeklySamplingOverJson(jsonObject):
    if "days" not in jsonObject:
        return

    jsonResult = deepcopy(jsonObject)

    week_data = {}

    for day in jsonResult["days"]:
        if "datetime" in day:
            date_obj = datetime.strptime(day["datetime"], "%Y-%m-%d")
            year_week = (date_obj.isocalendar().year, date_obj.isocalendar().week)

            if year_week not in week_data:
                week_data[year_week] = day

    jsonResult["days"] = list(week_data.values())

    return jsonResult

def stratifiedSamplingOverJson(jsonObject):
    if "days" not in jsonObject:
        return
    
    jsonResult = deepcopy(jsonObject)
    
    
    
    return jsonResult
    
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_dir = os.path.join(current_dir, 'json')
    
    input_file = os.path.join(json_dir,"weather-clean.json")
    random_sampling_file = os.path.join(json_dir,"weather-random-sampling.json")
    periodic_sampling_file = os.path.join(json_dir,"weather-periodic-sampling.json")
    stratified_file = os.path.join(json_dir,"weather-stratified-sampling.json")
    
    data = None
    random = None
    periodic = None
    stratified = None
    with open(input_file, 'r') as file:
        data = json.load(file)
        computeMeanOverJson(data)
        random = randomSamplingOverJson(data,2)
        periodic = weeklySamplingOverJson(data)
    
    if (random != None):
        with open(random_sampling_file, 'w') as file:
            json.dump(random, file, indent=4)
    
    if (periodic != None):
        with open(periodic_sampling_file, 'w') as file:
            json.dump(periodic, file, indent=4)
    
    if (stratified != None):
        with open(stratified_file, 'w') as file:
            json.dump(stratified, file, indent=4)