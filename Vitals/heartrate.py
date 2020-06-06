import numpy.random as np
import time

# returns a heartRate in BPM
def getHeartRate(stressed=False):
    heartRate = np.normal(loc=90, scale=20)
    heartRate = round(heartRate)
    if stressed == True:
        heartRate + 20
    return heartRate


def monitor(run_flag):
    while run_flag.value:
        time.sleep(1)
        curHeartRate = getHeartRate()
        if curRate < 35 or curRate > 200:
            print("Oha mein Herz")

def test():
    for i in range(1000):
        curRate = getHeartRate()
        print(curRate)
        if curRate < 35 or curRate > 200:
            print("Uff, autsch, mein Herz")


if __name__ == "__main__":
    test()
