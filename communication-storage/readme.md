# Labs 3 - Communication and Storage

## Communication

### MQTT

I generated 3 dataset using generateData.py, thay appear in the dedicated folder, the third one need to be uncommented if you want it. I commented it because the dataset is really fat (almost 2 Gb).

Then launch the docker compose, the adress of the broker is localhost:1883 but for the mqtt-explorer (UI on port 4000) use adress mqtt:mqtt-broker:1883 (container name instead of localhost).

Then you can send the data to the broker using sendDataMqtt.py, each message is apporximately 55 bytes. To that we must add between 2 and 12 bytes depending on the types of the message but here it's a publish message so it's only 2 bytes.

So for mqtt a message is approximately 57 bytes.

### HTTP

Here I used the same dataset that I used for MQTT. I launch a flask server with webserver.py, and then I send data with sendDataHttp.py, the server then return the size of the incoming packet and return it to the client so he can print it.

Here the payload size is the same around 55 bytes, but what is important is the size of the headers, with them we're around 200 bytes. So for small messages Mqtt is superior by far.

### Conclusion

Here using MQTT allow us to have message 75% smaller than when we used HTTP only due to the headers.