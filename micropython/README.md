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