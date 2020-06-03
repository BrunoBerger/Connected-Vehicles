from tkinter import *

from UI import buttonFunctions as bf

# Setup tkinter window and buttons
def spawnControlWindow(args, run_flag, all_processes):
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

    # generate Buttons and attach Function from the sibling-script
    b_test = Button(config, text="Print Something",
        command=lambda: bf.callbackTest(),
        height=2, width=15)
    b_npc = Button(config, text="Add NPCs",
        command= lambda: bf.initSpawnNPC(args, run_flag,
                                         all_processes,
                                         sl_numOfNpc),
        height=2, width=15)
    b_man = Button(config, text="Spawn a Manual Driver",
        command= lambda: bf.addManualDriver(args, all_processes),
        height=2, width=15)
    b_kill = Button(config, text="Delete Everybody",
        command= lambda: bf.killActors(run_flag, all_processes),
        height=2, width=15)

    # Slider to adjust the number of NPCs that will get spawned
    sl_numOfNpc = Scale(config, from_=1, to=100, orient=HORIZONTAL)
    sl_numOfNpc.set(args.number_of_vehicles)

    # Set position and attach to Tk window
    b_test.place(x = 30, y = 20)
    b_npc.place(x = 30, y = 70)
    b_man.place(x = 30, y = 120)
    b_kill.place(x = 30, y = 170)
    sl_numOfNpc.place(x = 150, y = 70)

    mainloop()
if __name__ == "__main__":
   pass
