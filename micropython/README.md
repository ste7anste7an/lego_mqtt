# MQTT implementation for MicroPython

(https://github.com/RuiSantosdotme/ESP-MicroPython.git)

Save the `umqttsimple.py` to the ESP32.

# Wifi credentials

Create a file `wifi_password.py` on the ESP32 containing:

```
wifi_ssid='<your ssid>'
wifi_password='<your wifi password>'
```

replacing `<your ssid>` and `<your wifi password>` with your wifi credentials. 

# mqtt_timing.py

This is a small demo application for syncing multiple ESP modules to an NTP server. 

We use the following MQTT channels

- `robot/notify`
  for sending raw messages `ntp` and `time`. The `ntp` message causes the client to resync with NTP, the `time` messages forces the client to publish the localtime and time milliseconds in the channe; `robot/time/<client_id>/time` and `robot/time/<client_id>/time_ms` with `<client_id>` a unique id (MAC address) of the client.
  
- `robot/time`
See above
- `robot/stats`
 Per robot a counter is shown
 
 ![image](https://user-images.githubusercontent.com/51531682/170205816-c9e68293-b71e-483d-a204-75a46403b7f7.png)
