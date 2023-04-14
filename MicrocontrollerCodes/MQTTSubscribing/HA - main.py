from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep
import esp32

## >mqtt client setup
#CLIENT_NAME = 'ESP32_2'
#BROKER_ADDR = '192.168.23.171'
#port = '1883'
#mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, port, keepalive=60)
#mqttc.connect()

## >sub_topic setup
#SUB_TOPIC = 'everything/smart/home'

## >callback function
#def sub_test(topic, msg):
#    if msg.decode() == '1':
#        print('Yellow')
#    else:
#        print('Blue')

## >mqtt subscription
#mqttc.set_callback(sub_test)
#mqttc.subscribe(SUB_TOPIC)

# >checking the message
#while True:
#    mqttc.check_msg()
#    sleep(0.5)
