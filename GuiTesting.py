from tkinter import *
from tkinter.ttk import *


number = int(input("Enter a number:\n"))



window = Tk()
window.title("Spreadsheet")
window.geometry("1000x1000")

i = number
while True:
     target = Button(window,width=10,text="Target")
     target.grid(column=i, row=i)
     i += 1
     if i > 1000:
         i = number
     if i < 10:
         i = number
         
    

