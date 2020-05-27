from tkinter import *
import os
import multiprocessing

import spawn_npc

# Tests Buttton Function
def callbackTest():
    print("Autsch")
# Spawns NPC into the world
def initSpawnNPC(args, run_flag, all_processes):
    print("Spawning NPC")
    run_flag.value = True
    process = multiprocessing.Process(target=spawn_npc.main, args=(args, run_flag,))
    process.start()
    all_processes.append(process)

def killNPC(args, run_flag, all_processes):
    print("Destroying NPCs")
    # close loose threads
    run_flag.value = False
    for process in all_processes:
        process.join()

def spawnControl(args, run_flag, all_processes):
    # generate tkinter-window
    config = Tk()
    config.title("Spawn Control")
    config.minsize(280,300)
    config.maxsize(350,600)
    # Gets the requested values of the height and widht.
    windowWidth = config.winfo_reqwidth()
    windowHeight = config.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(config.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(config.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    config.geometry("+{}+{}".format(positionRight, positionDown))

    # generate Buttons
    b_test = Button(config, text="Print Something",
        command=lambda: callbackTest(),
        height=2, width=15)
    b_start = Button(config, text="Spawn NPCs",
        command= lambda: initSpawnNPC(args, run_flag, all_processes),
        height=2, width=15)
    b_end = Button(config, text="Spawn a Manual Driver",
        command= lambda: callbackTest(),
        height=2, width=15)
    b_map = Button(config, text="Delete Everybody",
        command= lambda: killNPC(args, run_flag, all_processes),
        height=2, width=15)

    # Set position and attach to Tk window
    b_test.place(x = 30, y = 20)
    b_start.place(x = 30, y = 70)
    b_end.place(x = 30, y = 120)
    b_map.place(x = 30, y = 170)

    mainloop()

if __name__ == "__main__":
   pass
