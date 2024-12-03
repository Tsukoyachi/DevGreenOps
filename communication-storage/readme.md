# Labs 3 - Communication and Storage

## Communication

### MQTT

I generated 3 dataset using generateData.py, thay appear in the dedicated folder, the third one need to be uncommented if you want it. I commented it because the dataset is really fat (almost 2 Gb).

Then launch the docker compose, the adress of the broker is localhost:1883 but for the mqtt-explorer (UI on port 4000) use adress mqtt:mqtt-broker:1883 (container name instead of localhost).

Then you can send the data to the broker using sendData.py, each message is apporximately 55 bytes.