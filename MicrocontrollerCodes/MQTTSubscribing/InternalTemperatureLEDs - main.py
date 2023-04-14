from umqtt.simple import MQTTClient
import machine
import time
import esp32
from machine import Pin
from time import sleep

##LED Setup
led1 = machine.Pin(17, machine.Pin.OUT)
led2 = machine.Pin(18, machine.Pin.OUT)
led3 = machine.Pin(19, machine.Pin.OUT)

##>mqtt client setup
CLIENT_NAME = 'ESP32_2'
BROKER_ADDR = '192.168.11.171'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

# >sub_topic setup
SUB_TOPIC = 'int/temp'

# >callback function
def sub_test(topic, msg):
    print(msg.decode())
    if msg.decode() <= '54.0':
        led1.value(1)
        sleep(1)
        led1.value(0)
    elif msg.decode() <= '55.0':
        led2.value(1)
        sleep(0.5)
        led2.value(0)
    else:
        led3.value(1)
        sleep(5)
        led3.value(0)

# >mqtt subscription
mqttc.set_callback(sub_test)
mqttc.subscribe(SUB_TOPIC)

# >checking the message
while True:
    mqttc.check_msg()
    sleep(0.5)
