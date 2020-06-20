from tkinter import *
from tkinter.ttk import *
import random
from functools import partial



def press(bombs,box,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress):
    if firstpress == 0:
        bombplacer(bombs,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16)
        firstpress = 1
    

    
    i = 0
    boxvalue = 0
    while i < len(bombs):
        if bombs[i] == box - 1:
            boxvalue += 1
        if bombs[i] == box + 1:
            boxvalue += 1
        if bombs[i] == box + 3:
            boxvalue += 1
        if bombs[i] == box + 4:
            boxvalue += 1
        if bombs[i] == box + 5:
            boxvalue += 1
        if bombs[i] == box - 3:
            boxvalue += 1
        if bombs[i] == box - 4:
            boxvalue += 1
        if bombs[i] == box - 5:
            boxvalue += 1
        i += 1

    print(box)
    if box == 1:
        box1["text"] = boxvalue
    if box == 2:
        box2["text"] = boxvalue
    if box == 3:
        box3["text"] = boxvalue
    if box == 4:
        box4["text"] = boxvalue
    if box == 5:
        box5["text"] = boxvalue
    if box == 6:
        box6["text"] = boxvalue
    if box == 7:
        box7["text"] = boxvalue
    if box == 8:
        box8["text"] = boxvalue
    if box == 9:
        box9["text"] = boxvalue
    if box == 10:
        box10["text"] = boxvalue
    if box == 11:
        box11["text"] = boxvalue
    if box == 12:
        box12["text"] = boxvalue
    if box == 13:
        box13["text"] = boxvalue
    if box == 14:
        box14["text"] = boxvalue
    if box == 15:
        box15["text"] = boxvalue
    if box == 16:
        box16["text"] = boxvalue


def bomb():
    print("Boom!")

    
def windowmaker():

    #Window Settings
    root = Tk()
    root.title("Minesweeper")
    root.geometry('300x100')
    bombs = []
    firstpress = 0

    box1 = Button(root)
    box2 = Button(root)
    box3 = Button(root)
    box4 = Button(root)
    box5 = Button(root)
    box6 = Button(root)
    box7 = Button(root)
    box8 = Button(root)
    box9 = Button(root)
    box10 = Button(root)
    box11 = Button(root)
    box12 = Button(root)
    box13 = Button(root)
    box14 = Button(root)
    box15 = Button(root)
    box16 = Button(root)
    box1["command"] = partial(press, bombs, 1,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box2["command"] = partial(press, bombs, 2,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box3["command"] = partial(press, bombs, 3,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box4["command"] = partial(press, bombs, 4,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box5["command"] = partial(press, bombs, 5,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box6["command"] = partial(press, bombs, 6,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box7["command"] = partial(press, bombs, 7,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box8["command"] = partial(press, bombs, 8,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box9["command"] = partial(press, bombs, 9,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box10["command"] = partial(press, bombs, 10,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box11["command"] = partial(press, bombs, 11,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box12["command"] = partial(press, bombs, 12,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box13["command"] = partial(press, bombs, 13,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box14["command"] = partial(press, bombs, 14,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box15["command"] = partial(press, bombs, 15,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    box16["command"] = partial(press, bombs, 16,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,firstpress)
    

    box1.grid(column=0,row=0)
    box2.grid(column=1,row=0)
    box3.grid(column=2,row=0)
    box4.grid(column=3,row=0)
    box5.grid(column=0,row=1)
    box6.grid(column=1,row=1)
    box7.grid(column=2,row=1)
    box8.grid(column=3,row=1)
    box9.grid(column=0,row=2)
    box10.grid(column=1,row=2)
    box11.grid(column=2,row=2)
    box12.grid(column=3,row=2)
    box13.grid(column=0,row=3)
    box14.grid(column=1,row=3)
    box15.grid(column=2,row=3)
    box16.grid(column=3,row=3)

    root.mainloop()

    
def bombplacer(bombs,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16):
    boxtotal = 16
    bombtotal = 3
    a = 0
    i = 0

    if bombtotal > boxtotal:
        bombtotal = boxtotal - 1

    while len(bombs) < bombtotal:
        i = 0
        newbomb = random.randint(1, boxtotal)
        if len(bombs) == 0:
            bombs.append(newbomb)
        else:
            while i < len(bombs):
                if newbomb == bombs[i]:
                    newbomb = random.randint(1, boxtotal)
                    i = 0
                else:
                    i += 1
            else:
                bombs.append(newbomb)
                i = 0
                 
    a = 0
    i = len(bombs) - 1
    while a < len(bombs):
        print("Set {} to state: bomb".format(bombs[i]))
        if bombs[i] == 1:
            box1["text"] = "bomb"
            box1["command"] = bomb
        elif bombs[i] == 2:
            box2["text"] = "bomb"
            box2["command"] = bomb
        elif bombs[i] == 3:
            box3["text"] = "bomb"
            box3["command"] = bomb
        elif bombs[i] == 4:
            box4["text"] = "bomb"
            box4["command"] = bomb
        elif bombs[i] == 5:
            box5["text"] = "bomb"
            box5["command"] = bomb
        elif bombs[i] == 6:
            box6["text"] = "bomb"
            box6["command"] = bomb
        elif bombs[i] == 7:
            box7["text"] = "bomb"
            box7["command"] = bomb
        elif bombs[i] == 8:
            box8["text"] = "bomb"
            box8["command"] = bomb
        elif bombs[i] == 9:
            box9["text"] = "bomb"
            box9["command"] = bomb
        elif bombs[i] == 10:
            box10["text"] = "bomb"
            box10["command"] = bomb
        elif bombs[i] == 11:
            box11["text"] = "bomb"
            box11["command"] = bomb
        elif bombs[i] == 12:
            box12["text"] = "bomb"
            box12["command"] = bomb
        elif bombs[i] == 13:
            box13["text"] = "bomb"
            box13["command"] = bomb
        elif bombs[i] == 14:
            box14["text"] = "bomb"
            box14["command"] = bomb
        elif bombs[i] == 15:
            box15["text"] = "bomb"
            box15["command"] = bomb
        elif bombs[i] == 16:
            box16["text"] = "bomb"
            box16["command"] = bomb
        i -= 1
        a += 1
        
    print(bombs)


windowmaker()




