from tkinter import *

from tkinter.ttk import *

#Window Settings
window = Tk()
window.title("Klenner's Pizza shop")
window.geometry('800x400')
#header = Label(window,text="Klenner's Pizza Shop Online Ordering Tool:",font=("Arial Bold", 22))
#header.grid(column=0, row=0)

#Amount of pizzas
def PizzaAmountSetter():
    
    def PizzaAmountLockin():
        print("Good")
        PizzaAmountText.configure(text="{}".format(PizzaAmount.get()))
        PizzaAmountText.grid(column=1, row=1)
        PizzaAmountConfirm.destroy

    PizzaAmountText = Label(window,text="How many pizza's do you want?",font=("Arial Bold", 18))
    PizzaAmountText.grid(column=0, row=1)
    PizzaAmount = Entry(window,width=10)
    PizzaAmount.grid(column=1, row=1)
    PizzaAmount.focus()
    PizzaAmountConfirm = Button(window,width=10,text="Confirm",command=PizzaAmountLockin)
    PizzaAmountConfirm.grid(column=2, row=1)




#Pizza Flavour Picker
def pizzaFlavour():
    f1 = Radiobutton(window,text='First', value=1)
    f2 = Radiobutton(window,text='Second', value=2)
    f3 = Radiobutton(window,text='Third', value=3)
    f1.grid(column=1, row=2)
    f2.grid(column=2, row=2)
    f3.grid(column=3, row=2)


PizzaAmountSetter()
window.mainloop()
