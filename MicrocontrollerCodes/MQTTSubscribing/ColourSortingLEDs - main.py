## Colour sorting LEDs

from umqtt.simple import MQTTClient
import machine
import time
import esp32
from machine import Pin
from time import sleep

##> LED order setup
r = machine.Pin(18, machine.Pin.OUT)
g = machine.Pin(19, machine.Pin.OUT)
b = machine.Pin(17, machine.Pin.OUT)

##>mqtt client setup
CLIENT_NAME = 'ESP32_2'
BROKER_ADDR = '192.168.19.171'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

##>sub_topic setup
SUB_TOPIC = '/color'

##>callback function
def sub_test(topic, msg):
    print(msg.decode())
    text=msg.decode()
    data=text.split(',')
    #print(data[0])
    redraw=(data[0]).split('=')
    #print(red[1])
    greenraw=(data[1]).split('=')
    #print(green[1])
    blueraw=(data[2]).split('=')
    #print(blue[1])
    red=int(redraw[1])
    green=int(greenraw[1])
    blue=int(blueraw[1])

    if green<red and blue<red:
        g.value(0)
        b.value(0)
        r.value(1)
        print('red')
    elif red<green and blue<green:
        g.value(1)
        b.value(0)
        r.value(0)
        print('green')
    elif green<blue and red<blue:
        g.value(0)
        b.value(1)
        r.value(0)
        print('blue')
    else:
        g.value(0)
        b.value(0)
        r.value(0)
        print('colour undefined')        
 
##>mqtt subscription
mqttc.set_callback(sub_test)
mqttc.subscribe(SUB_TOPIC)

##>checking the message
while True:
    mqttc.check_msg()
    sleep(0.5)
