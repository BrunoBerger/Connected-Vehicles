import multiprocessing
import time

import spawn_npc
import manual_control
from UI import interface

# Spawns NPC into the world
def initSpawnNPC(args, run_flag, all_processes, sl_numOfNpc):

    newVal = sl_numOfNpc.get()
    args.number_of_vehicles = newVal
    print("Spawning", newVal, "NPCs")

    run_flag.value = True
    process = multiprocessing.Process(target=spawn_npc.main, args=(args, run_flag,))
    process.start()
    all_processes.append(process)

# destroys all cars
def killActors(run_flag, all_processes):
    print("Destroying NPCs")
    # close all threads
    run_flag.value = False
    for process in all_processes:
        process.join()

# Spawns a manualy driven Car,
# that will communicate with the smart city
def addManualDriver(args, all_processes, b_man):
    # b_man.config(state="disabled")
    carProcess = multiprocessing.Process(target=manual_control.main,
                                         args=(args, all_processes))
    # carProcess.daemon = True
    carProcess.start()
