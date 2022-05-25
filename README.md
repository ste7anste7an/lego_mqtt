# lego_mqtt
MQTT implementation for a swarm of Lego robots

# MQTT protocol

The Message Queuing Telemetry Transport (MQTT) protocol is a light weigth publish-subscribe messaging protocol designed in the late 90s. 

MQTT is:
- Agnostic with respect to the content of the message
- Ideal for one-to-many communication distribution and decoupled applications
- Equipped with a “last will and testament” feature to notify parties of abnormal client disconnection
- Dependent on TCP/IP for basic connectivity purposes
- Designed for at most once, at least once and exactly once message delivery

In MQTT a central role is played by the so-called broker. The broker is responsible for distributing messages published by a publisher among the subscriber clients that subscribe to a specific message branch. In MQTT channels are defined by a path-like structure e.g.

```
robots/robotid/power
```
