import numpy.random as np
import time

# returns a heartRate in BPM
def getHeartRate(stressed=False):
    heartRate = np.normal(loc=90, scale=20)
    heartRate = round(heartRate)
    if stressed == True:
        heartRate + 20
    return heartRate


def monitor():
    set
    while run_flag.value:
        time.sleep(1)
        curHeartRate = getHeartRate()


def test():
    for i in range(200):
        curRate = getHeartRate()
        print(curRate)
        if curRate < 40 or curRate > 140:
            print("     Go to the doc!")


if __name__ == "__main__":
    test()
