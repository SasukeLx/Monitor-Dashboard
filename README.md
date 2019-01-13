# Monitor-Dashboard
  用于基于流量传感器的静脉输液流速监测的客户端
  
##1、组成部分
  程序主要由Raspberry Pi的I2C通信程序和MQTT客户端，以及PC端基于Node.js实现MQTT协议的APP构成，采用百度天工IoT接入实现数据服务端。
  
##2、运行环境
  Raspbian : Python、WiringPi、I2ctools、Paho-mqtt
  Windows: Node.js、mqtt.js、node-red
