import multiprocessing
import argparse
import time

from mqtt_Tests import listen
from UI import interface
import arguments

def main():
    print("Loading args and UI")
    # init launch-options
    args = arguments.defaultArgs()

    # to control and keep track of all threads
    run_flag = multiprocessing.Value('I', True)
    all_processes = []

    # # Keep listening to the server
    # print("Listenting to server")
    # process = multiprocessing.Process(target=listen.connect, args=(run_flag,))
    # process.start()
    # all_processes.append(process)


    # generate window to control the spawning of vehicles
    interface.spawnControlWindow(args, run_flag, all_processes)

    # close loose threads
    run_flag.value = False
    for process in all_processes:
        process.join()
    print("Process Terminated")
    print("done")


if __name__ == "__main__":
   main()
