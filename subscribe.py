import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.on_subscribe = on_subscribe

host = 'm14.cloudmqtt.com'
port = 17419
topic = 'test'
username = 'hufvczek'
password = 'Jxv8I_AvjN7S'

mqttc.username_pw_set(username, password)
mqttc.connect(host, port)
mqttc.subscribe(topic, 0)


rc = 0
while rc == 0:
	rc = mqttc.loop()
