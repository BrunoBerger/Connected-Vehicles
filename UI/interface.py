from tkinter import *

from UI import buttonFunctions as bf

# Setup tkinter window and buttons
def spawnControlWindow(args, run_flag, all_processes):
    # generate tkinter-window
    master = Tk()
    master.title("Spawn Control")
    master.minsize(280,250)
    master.maxsize(280,250)
    # Gets both half the screen width/height and window width/height
    positionRight = int(master.winfo_screenwidth()/1.5)
    positionDown = int(master.winfo_screenheight()/2.5)
    # Positions the window in the center of the page.
    master.geometry("+{}+{}".format(positionRight, positionDown))

    # generate Buttons and attach Function from the sibling-script
    buttonColour = "light blue"
    b_npc = Button(master, text="Add NPCs",
        command= lambda: bf.initSpawnNPC(args, run_flag,
                                         all_processes,
                                         sl_numOfNpc),
        height=4, width=15, bg=buttonColour)
    b_man = Button(master, text="Spawn a Manual Driver",
        command= lambda: bf.addManualDriver(args, all_processes, b_man),
        height=3, width=20, bg=buttonColour)
    b_kill = Button(master, text="Delete Everybody",
        command= lambda: bf.killActors(run_flag, all_processes),
        height=1, width=13, bg=buttonColour)

    # Slider to adjust the number of NPCs that will get spawned
    sl_numOfNpc = Scale(master, from_=1, to=100, orient=HORIZONTAL)
    sl_numOfNpc.set(args.number_of_vehicles)

    # Labels
    l_github = Label(master, text="View this project on GitHub", fg="blue")
    l_github.bind("<Button-1>",
        lambda e: bf.openWeblink("https://github.com/BrunoBerger/Connected-Vehicles"))

    # Set position and attach to Tk window
    b_npc.place(x = 30, y = 20)
    b_man.place(x = 56, y = 120)
    b_kill.place(x = 153, y = 58)
    sl_numOfNpc.place(x = 150, y = 10)
    l_github.place(x = 60, y = 220)

    mainloop()
if __name__ == "__main__":
   pass
