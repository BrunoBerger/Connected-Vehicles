
import paho.mqtt.client as mqtt
import time

from Vitals import heartrate

#Methode um Daten zu senden
def sendData(mqttClient):
    stressed = True
    vitals = heartrate.getHeartRate(stressed)
    print("My heart-Rate is ", vitals, " BPM")

    topic = "/hshl/test"
    payLoad = "[TEST] help, i crashed my car"
    print("Sending data now")
    mqttClient.publish(topic, payLoad)
    mqttClient.loop_start()
    time.sleep(0.1)
    mqttClient.loop_stop()

#Event, dass beim Verbindungsaufbau aufgerufen wird
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)

def connectToCity():
    #Dont change anything from here!!
    BROKER_ADDRESS = "mr2mbqbl71a4vf.messaging.solace.cloud" #Adresse des MQTT Brokers
    mqttClient = mqtt.Client()
    mqttClient.on_connect = on_connect #Zuweisen des Connect Events
    mqttClient.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha") # Benutzernamen und Passwort zur Verbindung setzen
    mqttClient.connect(BROKER_ADDRESS, port = 20614) #Verbindung zum Broker aufbauen

    return mqttClient
