# -------------------
# Imports stuff here
# -------------------
import tkinter as tk
import random

# creates the window instance
win = tk.Tk()

# adds a title
win.title("Dungeons & Dragons Dice Roller")

# adds a frame that our widgets are going to be contained within
mainFrame = tk.Frame(win)
mainFrame.pack()

rollSection = tk.Listbox(win)
rollSection.pack()


def roll(dice):
    dicelabel = tk.Label(rollSection, text=("You rolled a " + str(random.randint(1, dice))))
    dicelabel.pack()


# creating button and label widgets
tk.Label(mainFrame, text="Welcome to the D&D Roller").pack()
roll20 = tk.Button(mainFrame, text="Roll a d20", command=lambda: roll(20))
roll12 = tk.Button(mainFrame, text="Roll a d12", command=lambda: roll(12))
roll10 = tk.Button(mainFrame, text="Roll a d10", command=lambda: roll(10))
roll6 = tk.Button(mainFrame, text="Roll a d6", command=lambda: roll(6))
roll4 = tk.Button(mainFrame, text="Roll a d4", command=lambda: roll(4))
roll20.pack()
roll12.pack()
roll10.pack()
roll6.pack()
roll4.pack()
# creates the main loop
win.mainloop()
