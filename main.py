import random
import time
import tkinter as tk
import tkinter.font as tkFont
hmm = ""

Tk = tk.Tk()
# setting title
Tk.title("Rock-Paper-Scissor")
# setting window size
width = 491
height = 250
screenwidth = Tk.winfo_screenwidth()
screenheight = Tk.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
Tk.geometry(alignstr)
Tk.resizable(width=False, height=False)
Tk.iconphoto = "icon.ico"
# Tk.configure(background = "yellow")


def rock_command():
    n = random.randint(1, 6)
    if n <= 2:
        opponent.config(text="Rock")
        result.config(text="Tie!")
    elif n <= 4:
        opponent.config(text="scissor")
        result.config(text="You Won!")
    else:
        opponent.config(text="Paper")
        result.config(text="Opponent Won!")


def paper_command():
    n = random.randint(1, 6)
    if n <= 2:
        opponent.config(text="Rock")
        result.config(text="You Won!")
    elif n <= 4:
        opponent.config(text="scissor")
        result.config(text="Opponent Won!")
    else:
        opponent.config(text="Paper")
        result.config(text="Tie!")


def scissor_command():
    n = random.randint(1, 6)
    if n <= 2:
        opponent.config(text="Rock")
        result.config(text="Opponent Won!")
    elif n <= 4:
        opponent.config(text="scissor")
        result.config(text="Tie!")
    else:
        opponent.config(text="Paper")
        result.config(text="You Won!")


rock = tk.Button(Tk)
rock["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
rock["font"] = ft
rock["fg"] = "#000000"
rock["justify"] = "center"
rock["text"] = "Rock"
rock.place(x=30, y=60, width=181, height=30)
rock["command"] = rock_command

paper = tk.Button(Tk)
paper["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
paper["font"] = ft
paper["fg"] = "#000000"
paper["justify"] = "center"
paper["text"] = "Paper"
paper.place(x=30, y=100, width=181, height=30)
paper["command"] = paper_command

scissor = tk.Button(Tk)
scissor["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
scissor["font"] = ft
scissor["fg"] = "#000000"
scissor["justify"] = "center"
scissor["text"] = "Scissor"
scissor.place(x=30, y=140, width=180, height=30)
scissor["command"] = scissor_command

GLabel_650 = tk.Label(Tk)
ft = tkFont.Font(family='Times', size=28)
GLabel_650["font"] = ft
GLabel_650["fg"] = "#333333"
GLabel_650["justify"] = "center"
GLabel_650["text"] = "Rock-Paper-Scissor"
GLabel_650.place(x=30, y=10, width=448, height=30)

GLabel_617 = tk.Label(Tk)
ft = tkFont.Font(family='Times', size=18)
GLabel_617["font"] = ft
GLabel_617["fg"] = "#333333"
GLabel_617["justify"] = "center"
GLabel_617["text"] = "Opponent"
GLabel_617.place(x=280, y=60, width=173, height=30)

opponent = tk.Label(Tk)
ft = tkFont.Font(family='Times', size=33)
opponent["font"] = ft
opponent["fg"] = "#333333"
opponent["justify"] = "center"
opponent["text"] = ""
opponent.place(x=250, y=100, width=228, height=67)

result = tk.Label(Tk)
ft = tkFont.Font(family='Times', size=18)
result["font"] = ft
result["fg"] = "#333333"
result["justify"] = "center"
result["text"] = ""
result.place(x=130, y=200, width=230, height=30)

if __name__ == "__main__":
    Tk.mainloop()

# pyinstaller --onefile --windowed --icon=icon.ico main.py
