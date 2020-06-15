import multiprocessing
import argparse
import time
import os

from Communication import listen
from UI import interface
from assets import arguments

def main():
    # Set current working dir to the one of main.pyq
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    print("Loading args and UI")
    # init launch-options
    args = arguments.defaultArgs()

    # to control and keep track of all threads
    run_flag = multiprocessing.Value('I', True)
    all_processes = []

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
