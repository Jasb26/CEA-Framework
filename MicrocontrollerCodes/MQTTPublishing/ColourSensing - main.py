from machine import Pin
import time
import machine
from umqtt.simple import MQTTClient

################### Publishing Colour Data

led = machine.Pin(17, machine.Pin.OUT)
led.value(1)

def wait_for_edge(pin):
    global edge
    edge = True

def measure():
    global edge
    delta = 0
    time.sleep(0.1)
    start = time.ticks_us()
    for i in range(10):
        edge = False
        while (edge == False):
            pass
    delta = time.ticks_diff(time.ticks_us(), start)
    return delta


CLIENT_NAME = 'color_meter'
BROKER_ADDR = '192.168.19.171'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

TOPIC = b'/color'

GPIO_S0  = 16 # switched from 15
GPIO_S1  =  4
GPIO_S2  =  5
GPIO_S3  = 18
GPIO_OUT = 19

pS0  = Pin(GPIO_S0, Pin.OUT)
pS1  = Pin(GPIO_S1, Pin.OUT)
pS2  = Pin(GPIO_S2, Pin.OUT)
pS3  = Pin(GPIO_S3, Pin.OUT)
pOUT = Pin(GPIO_OUT, Pin.IN, Pin.PULL_UP)

pS0.on()
pS1.on()

pOUT.irq(trigger=Pin.IRQ_FALLING, handler=wait_for_edge)


while (True):
    pS2.off()
    pS3.off()
    red = measure()

    pS2.off()
    pS3.on()
    blue = measure()
    
    pS2.on()
    pS3.on()
    green = measure()

    msg = 'clr_lvl red=' + str(red) + ',' + 'green=' + str(green) + ',' + 'blue=' + str(blue)
    mqttc.publish(TOPIC, msg.encode())

    if green < red and blue < red:
        print("red")
        #temp = 1
    
    elif red < green and blue < green:
        print("green")
        #temp=1

    elif green < blue and red < blue:
        print("blue")
        #temp=1

    else:
        print("undefined")

