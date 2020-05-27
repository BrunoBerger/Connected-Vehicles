import multiprocessing
import argparse

import interface
import arguments

def main():
    args = arguments.defaultArgs()


    run_flag = multiprocessing.Value('I', True)
    all_processes = []

    interface.spawnControlWindow(args, run_flag, all_processes)


    # close loose threads
    run_flag.value = False
    for process in all_processes:
        process.join()
    print("Process Terminated")
    print("done")


if __name__ == "__main__":
   main()
