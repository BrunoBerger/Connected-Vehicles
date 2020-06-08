import paho.mqtt.client as mqtt
import time
import datetime

# Connect to the mqtt-Server
#Event, dass beim eintreffen einer Nachricht aufgerufen wird
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8")) #Nachricht Dekodieren
    currentDT = datetime.datetime.now() #Aktuelle Uhrzeit
    print(currentDT.strftime("%Y-%m-%d %H:%M:%S")+" Nachricht erhalten: "+str(msg))
    #Hier die Verarbeitung der Nachricht einfügen

#Event, dass beim Verbindungsaufbau aufgerufen wird
def on_connect(client, userdata, flags, rc):
    #Abonnieren des Topics (Hier die jeweiligen Topics einfügen die vorgegeben sind
    client.subscribe('/hshl/#')

def main():
    # Connect to solace server
    print("Trying to connect to mqtt Server")
    BROKER_ADDRESS = "mr2mbqbl71a4vf.messaging.solace.cloud" #Adresse des MQTT Brokers
    client = mqtt.Client()
    client.on_connect = on_connect #Zuweisen des Connect Events
    client.on_message = on_message #Zuweisen des Message Events
    client.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha") # Benutzernamen und Passwort zur Verbindung setzen
    client.connect(BROKER_ADDRESS, port = 20614) #Verbindung zum Broker aufbauen
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)

    client.loop_forever()

if __name__ == "__main__":
    main()
