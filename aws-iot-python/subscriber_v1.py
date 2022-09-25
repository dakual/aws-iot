import sys, ssl, os, time
import logging, traceback
import paho.mqtt.client as mqtt

endpoint = os.getenv('AWS_IOT_ENDPOINT')
clientid = "myDevice1"

ca       = "../AmazonRootCA1.pem" 
cert     = "../certificate.crt"
private  = "../private.key"

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(log_format)
logger.addHandler(handler)

def ssl_alpn():
    try:
        logger.info("open ssl version:{}".format(ssl.OPENSSL_VERSION))
        ssl_context = ssl.create_default_context()
        ssl_context.set_alpn_protocols(["x-amzn-mqtt-ca"])
        ssl_context.load_verify_locations(cafile=ca)
        ssl_context.load_cert_chain(certfile=cert, keyfile=private)

        return ssl_context
    except Exception as e:
        print("exception ssl_alpn()")
        raise e

def on_message_temperature(client, userdata, msg):
    print('Received a new temperature data ', msg.payload.decode('utf-8'))


def on_message_humidity(client, userdata, msg):
    print('Received a new humidity data ', str(msg.payload.decode('utf-8')))


if __name__ == '__main__':
    try:
        mqttc = mqtt.Client(clientid)
        mqttc.message_callback_add("myTopic/temp", on_message_temperature)
        mqttc.message_callback_add("myTopic/humi", on_message_humidity)
        ssl_context = ssl_alpn()
        mqttc.tls_set_context(context=ssl_context)
        logger.info("Connecting...")
        mqttc.connect(endpoint, port=8883)
        logger.info("Successfully connected!")
        mqttc.loop_start()

        mqttc.subscribe("myTopic/temp")
        logger.info("try to subscribe:{}".format("myTopic/temp"))

        mqttc.subscribe("myTopic/humi")
        logger.info("try to subscribe:{}".format("myTopic/humi"))

        while True:
            time.sleep(1)

    except Exception as e:
        logger.error("exception main()")
        logger.error("e obj:{}".format(vars(e)))
        logger.error("message:{}".format(e.message))
        traceback.print_exc(file=sys.stdout)


