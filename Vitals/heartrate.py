import numpy.random as np
import time

from Communication import mqttFunctions

# returns a heartRate in BPM
def getHeartRate(stressed=False):
    heartRate = np.normal(loc=90, scale=20)
    heartRate = round(heartRate)
    if stressed == True:
        heartRate + 20
    return heartRate


def monitor(monitor_flag):
    print("Monitoring Heartrate", flush=True)
    while monitor_flag.value:
        time.sleep(1)
        curRate = getHeartRate()
        if curRate < 35 or curRate > 200:

            topic = "/hshl/users/" + str(args.id)
            crashInfo = {
                "driver_name": args.rolename,
                "location": location,
                "reasons": "generic reason",
                "topic": topic
                }
            payLoad = json.dumps(crashInfo)
            mqttFunctions.sendData(mqttClient, topic, payLoad)

        else:
            print("Heartrate normal, at",curRate,"BPM", flush=True)

def test():
    for i in range(1000):
        curRate = getHeartRate()
        print(curRate)
        if curRate < 35 or curRate > 200:
            print("Uff, autsch, mein Herz")


if __name__ == "__main__":
    test()
