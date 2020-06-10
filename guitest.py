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
    pizza_total = 0
    custom_cost = []
    pizza_order = []
    drink_order = []
    custom_pizzas = []

    
    def PizzaAmountLockin():
        MainText.configure(text="{} pizzas selected".format(PizzaAmount.get()))
        MainText.grid(column=1, row=1)
        PizzaAmountConfirm.grid_forget()
        PizzaAmount.grid_forget()
        pizzaFlavour(MainText,pizza_total,custom_cost,pizza_order,custom_pizzas,drink_order)

    MainText = Label(window,text="How many pizza's do you want?",font=("Arial Bold", 18))
    MainText.grid(column=0, row=1)
    PizzaAmount = Entry(window,width=10)
    PizzaAmount.grid(column=1, row=1)
    PizzaAmount.focus()
    PizzaAmountConfirm = Button(window,width=10,text="Confirm",command=PizzaAmountLockin)
    PizzaAmountConfirm.grid(column=2, row=1)




#Pizza Flavour Picker
def pizzaFlavour(MainText,pizza_total,custom_cost,pizza_order,custom_pizzas,drink_order):
    btn1 = IntVar()
    def PizzaFlavourLockin():
        f1.grid_forget()
        f2.grid_forget()
        f3.grid_forget()
        f4.grid_forget()
        PizzaFlavourConfirm.grid_forget()
        flavour = btn1.get()
        print(flavour)
        if flavour == 1:
            MainText.configure(text="Pepperoni pizza selected")
            pizza_order.append(1)
            PizzaFlavourConfirm2.grid(column=1, row=2)
            PizzaFlavourConfirm2 = Button(window,width=10,text="Confirm",command=pizzaFlavour)
        elif flavour == 2:
            MainText.configure(text="Hawaiian pizza selected")
            pizza_order.append(2)
            PizzaFlavourConfirm2 = Button(window,width=10,text="Confirm",command=pizzaFlavour)
            PizzaFlavourConfirm2.grid(column=1, row=2)
        elif flavour == 3:
            MainText.configure(text="Cheese pizza selected")
            pizza_order.append(3)
            PizzaFlavourConfirm2 = Button(window,width=10,text="Confirm",command=pizzaFlavour)
            PizzaFlavourConfirm2.grid(column=1, row=2)
        elif flavour == 4:
            MainText.configure(text="Custom pizza selected")

    
    f1 = Radiobutton(window,text='Pepperoni', value=1, variable = btn1)
    f2 = Radiobutton(window,text='Hawaiian', value=2, variable = btn1)
    f3 = Radiobutton(window,text='Cheese', value=3, variable = btn1)
    f4 = Radiobutton(window,text='Custom', value=4, variable = btn1)
    f1.grid(column=1, row=2)
    f2.grid(column=2, row=2)
    f3.grid(column=3, row=2)
    f4.grid(column=4, row=2)
    PizzaFlavourConfirm = Button(window,width=10,text="Confirm",command=PizzaFlavourLockin)
    PizzaFlavourConfirm.grid(column=5, row=2)


PizzaAmountSetter()
window.mainloop()
