import paho.mqtt.client as paho
import ssl, os
from time import sleep

isConnected = False

def on_connect(client, userdata, flags, rc):
    global isConnected
    isConnected = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode('utf-8'))

def on_log(client, userdata, level, buf):
    print(buf.topic + ": " + str(buf.payload))



awshost  = os.getenv('AWS_IOT_ENDPOINT')
awsport  = 8883
clientId = "myDevice1"

caPath   = "../AmazonRootCA1.pem"
certPath = "../certificate.crt"
keyPath  = "../private.key"

mqttc = paho.Client(clientId)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_log = on_log
mqttc.tls_set(
    caPath, 
    certfile=certPath, 
    keyfile=keyPath, 
    cert_reqs=ssl.CERT_REQUIRED, 
    tls_version=ssl.PROTOCOL_TLSv1_2, 
    ciphers=None)
mqttc.connect(awshost, awsport)
mqttc.loop_start()
mqttc.subscribe("myTopic/temp")

while True:
    sleep(1)
        