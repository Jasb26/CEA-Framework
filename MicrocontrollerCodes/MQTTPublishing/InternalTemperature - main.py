from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep
import esp32

##Publishes ESP32 Internal Temperature, in Celcius

CLIENT_NAME = 'ESP32'
BROKER_ADDR = '192.168.152.171'
port = '1883'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, port, keepalive=60)
mqttc.connect()

while True:
    Tf = esp32.raw_temperature()
    Tc = (Tf-32.0)/1.8
    msg = str(Tc)
    mqttc.publish(b'int/temp', msg.encode())
    sleep(10)
