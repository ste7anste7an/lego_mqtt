
import ntptime    
import time    
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()


# connect to wifi

# 
ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'



def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
do_connect()

def show_time(tns):
    ts=time.localtime(int(tns//1000000000))
    tus=(tns%1000000000)/1000
    print(ts,tus)

# set time to ntp time
ntptime.settime()

mqtt_server = '192.168.2.5'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
# generate unique client_id, might as well use last 4 digits.
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'robot/notify'
topic_pub = b'robot/time/'+client_id
topic_pub_stats= b'robot/stats/'+client_id

last_message = 0
message_interval = 5
counter = 0

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'robot/notify' and msg == b'ntp':
    print('ESP received hello message')
    ntptime.settime()
  if topic == b'robot/notify' and msg == b'time':
    # publish milli second part of time
    client.publish(topic_pub+b'/time', ("%d/%02d/%02d %02d:%02d:%02d"%(time.localtime()[:6])).encode('utf-8'))
    client.publish(topic_pub+b'/time_ms', ("%d"%((time.time_ns()%1000000000)//1000000)).encode('utf-8'))


def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  #machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      msg = b'Hello #%d' % counter
      client.publish(topic_pub_stats+b'/count', msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()