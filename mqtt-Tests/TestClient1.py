import paho.mqtt.client as mqtt
import time
import json

pizza = "salami"
quantity = 10

def on_message(client, userdata, message):
    print("Just got this message: " ,str(message.payload.decode("utf-8")))


data = {
    "name": "Bruno",
    "pizza": pizza,
    "quantity": quantity,
    "topic": "hshl/customer/myid",
}


client1 = mqtt.Client("myPC_testClient1")
client1.connect("broker.mqttdashboard.com")

print("Connected to HiveMQ-Server")

client1.subscribe("city/car", qos=0)
print("Subscribed to topic", "city/car")

client1.publish("city/car","HELLO THERE")
client1.publish("city/car", json.dumps(data))

client1.on_message=on_message

client1.loop_start()
time.sleep(3)
client1.loop_stop()
