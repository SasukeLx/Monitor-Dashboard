import math
import time
import wiringpi as wpi
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("mqtt client not find . Please install and retry")
    print("pip install paho-mqtt")

    
host = 'eqx6629.mqtt.iot.bj.baidubce.com'
port = 1883

username = 'eqx6629/sasukelx'
password = 'ckYUpQgFBQoJu0Zi'

rc=0

def on_connect(mqttClient,userdata,flags,rc):
    print('Connection return'+str(rc))
    mqttClient.loop_start()

def on_message(mqttClient,userdata,msg):
    print(msg.topic+" "+str(msg.payload))
    
def main():
    id = wpi.wiringPiI2CSetup(0x07)
    mqttClient = mqtt.Client()
    mqttClient.username_pw_set(username,password)
    mqttClient.on_connect = on_connect
    mqttClient.on_message = on_message
    mqttClient.connect(host,port,60)
    time.sleep(1)
    for i in range (1,10000):
        wpi.delay(800)
        temp = wpi.wiringPiI2CReadReg16(id,0x00)
        speed = temp/1000
        print(speed,'L/min')
        mqttClient.publish('data_reg',speed,0)
        
    while True:
        pass

if __name__ == '__main__':
    main()


