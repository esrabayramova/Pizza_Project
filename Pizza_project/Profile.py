from tkinter import *
import sqlite3
from Decorator import *
import datetime
import tkinter.messagebox

class Order:

    def __init__(self, root, name, prev):

        self.root = root
        self.root.geometry('500x400')
        self.root.title('Select an option: ')
        self.name = name
        self.prev = prev

        self.b1 = Button(self.root, text='Select from menu', width=20, bg='MistyRose3', fg='white', command = self.menuu).place(x=150, y=100)
        self.b2 = Button(self.root, text='Custom pizza', width=20, bg='MistyRose3', fg='white', command = self.customm).place(x=150, y=150)
        self.b3 = Button(self.root, text='Back', width=20, bg='MistyRose3', fg='white', command=self.cancel).place(x=150, y=200)
        self.b3 = Button(self.root, text='Quit', width=20, bg='MistyRose3', fg='white', command=self.root.quit).place(x=150, y=250)

    def menuu(self):
        m = Toplevel(self.root)
        con = sqlite3.connect('Users.db')
        cursor = con.cursor()

        cursor.execute('SELECT Order_id FROM User_orders WHERE Order_id = (SELECT MAX(Order_id) FROM User_orders)')
        order_id = cursor.fetchone()[0] + 1
        mc = Menu(m, self.name, order_id, self.root)
        self.root.withdraw()

    def customm(self):
        s = Toplevel(self.root)
        con = sqlite3.connect('Users.db')
        cursor = con.cursor()

        cursor.execute('SELECT Order_id FROM User_orders WHERE Order_id = (SELECT MAX(Order_id) FROM User_orders)')
        order_id = cursor.fetchone()[0] + 1
        sc = Custom_size(s, self.name, order_id, self.root)
        self.root.withdraw()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.withdraw()

class Menu:

    def __init__(self, master, name, order_id, prev):

        self.master = master
        self.master.geometry('1500x800')
        self.master.title("Main menu")
        #self.selected_pizaa = None
        self.name = name
        self.order_id = order_id
        self.prev = prev

        self.label_0 = Label(master, text = 'Pizzeria`s Traditionals', font=("bold", 20), fg='AntiqueWhite3')
        self.label_0.place(x=350, y=10)

        self.label_00 = Label(master, text = 'Latest updates', font=("bold", 20), fg='AntiqueWhite3')
        self.label_00.place(x=1000, y=10)

        self.r = IntVar()

        self.r1 = Radiobutton(master, text='Margherita Pizza\n35$', width=15, font=("Helvetica", 12, "italic"), variable=self.r, value=1).place(x=0, y=75)
        self.r2 = Radiobutton(master, text='Hawaiian Pizza\n45$', width=15, font=("Helvetica", 12, "italic"), variable=self.r, value=2).place(x=0, y=275)
        self.r3 = Radiobutton(master, text='Sicilian Pizza\n45$', width=15, font=("Helvetica", 12, "italic"), variable=self.r, value=3).place(x=0, y=475)
        self.r4 = Radiobutton(master, text='Pizza Vegetariana\n30$', width=15, font=("Helvetica", 12, "italic"), variable=self.r, value=4).place(x=410, y=75)
        self.r5 = Radiobutton(master, text='Mexican Taco Pizza\n65$', width=15, font=("Helvetica", 12, "italic"), variable=self.r, value=5).place(x=410, y=275)
        self.r6 = Radiobutton(master, text='Pizza Deluxe\n50$', width=15, font=("Helvetica", 12, "italic"), variable=self.r, value=6).place(x=410, y=475)

        self.img1 = PhotoImage(file='Pizzas_gif/margherita-pizza.gif')
        self.label_img1 = Label(master, image=self.img1).place(x=200, y=50)

        self.img2 = PhotoImage(file='Pizzas_gif/hawaiian-pizza.gif')
        self.label_img2 = Label(master, image=self.img2).place(x=200, y=250)

        self.img3 = PhotoImage(file='Pizzas_gif/sicilian-pizza.gif')
        self.label_img3 = Label(master, image=self.img3).place(x=200, y=450)

        self.img4 = PhotoImage(file='Pizzas_gif/pizza-vegetariana.gif')
        self.label_img4 = Label(master, image=self.img4).place(x=600, y=50)

        self.img5 = PhotoImage(file='Pizzas_gif/mexican-taco-pizza.gif')
        self.label_img5 = Label(master, image=self.img5).place(x = 600, y = 250)

        self.img6 = PhotoImage(file='Pizzas_gif/deluxe-pizza.gif')
        self.label_img6 = Label(master, image=self.img6).place(x= 600, y=450)

        con = sqlite3.connect('Pizzeria.db')
        cursor = con.cursor()
        cursor.execute('SELECT Pizza_id FROM Pizzas WHERE Pizza_id = (SELECT MAX(Pizza_id) FROM Pizzas)')
        id = cursor.fetchall()[0][0]
        #print(id)

        if id > 6:
            h = 20
            cursor.execute('SELECT Pizza FROM Pizzas WHERE Pizza_id > ?', (6, ))
            pza = cursor.fetchall()
            cursor.execute('SELECT Price FROM Pizzas WHERE Pizza_id > ?', (6,))
            pce = cursor.fetchall()
            #print(pza)
            n = len(pza)
            for i in range(0, n):
                Radiobutton(self.master, text = pza[i][0]+' - '+pce[i][0]+'$', width=20, font=("Helvetica", 12, "italic"), variable=self.r, value=7+i).place(x=900, y=100 + h)
                h += 50

        self.b1 = Button(master, text="Order", width=20, bg='MistyRose3', fg='white', command=self.pizza).place(x=350, y=700)
        self.b2 = Button(master, text="Back", width=20, bg='MistyRose3', fg='white', command=self.cancel).place(x=50, y=700)
        self.b3 = Button(master, text="Quit", width=20, bg='MistyRose3', fg='white', command=self.master.quit).place(x=650, y=700)

    def pizza(self):

        #self.master.quit()
        var = self.r.get()

        '''if var == 1:
            self.selected_pizaa = 'Margherita Pizza'

        elif var == 2:
            self.selected_pizaa = 'Hawaiian Pizza'

        elif var == 3:
            self.selected_pizaa = 'Sicilian Pizza'

        elif var == 4:
            self.selected_pizaa = 'Pizza Vegetariana'

        elif var == 5:
            self.selected_pizaa = 'Mexican Taco Pizza'

        elif var == 6:
            self.selected_pizaa = 'Pizza Deluxe'''

        #print(self.selected_pizaa)

        con = sqlite3.connect('Pizzeria.db')
        cursor = con.cursor()

        cursor.execute('SELECT Pizza FROM Pizzas WHERE Pizza_id = ?', (var, ))
        piza = cursor.fetchall()[0][0]

        cursor.execute('SELECT Ingredients FROM Pizzas WHERE Pizza_id = ?', (var,))
        ing = cursor.fetchall()[0][0]

        cursor.execute('SELECT Price FROM Pizzas WHERE Pizza_id = ?', (var,))
        prce = cursor.fetchall()[0][0]

        con.close()

        con = sqlite3.connect('Users.db')
        cursor = con.cursor()

        #print(piza)
        #print(ing)
        #print(prce)
        #print(var)

        cursor.execute('INSERT INTO User_orders(Username, Order_id) VALUES (?, ?)', (self.name, self.order_id))
        cursor.execute('INSERT INTO Orders(Order_id, Order_content, History, Price) VALUES (?, ?, ?, ?)', (self.order_id, piza+':'+ing, datetime.datetime.now(), prce))

        con.commit()
        con.close()
        tkinter.messagebox.showinfo('Info', 'Your submission has been received.')
        self.master.destroy()
        self.prev.update()
        self.prev.deiconify()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.master.withdraw()

class Custom_size:

    def __init__(self, master, name, order_id, prev):

        self.master = master
        self.master.geometry('750x650')
        self.master.title("Select size: ")
        self.pizza_size = None
        self.MyPizza = None
        self.name = name
        self.order_id = order_id
        self.prev = prev

        self.r = IntVar()
        self.r_1 = Radiobutton(master, text='Small - 10$', width=15, font=("Helvetica", 12, "italic"),
                               variable=self.r, value=1).place(x=25, y=300)
        self.r_2 = Radiobutton(master, text='Medium - 15$', width=15, font=("Helvetica", 12, "italic"),
                               variable=self.r, value=2).place(x=200, y = 300)
        self.r_3 = Radiobutton(master, text='Large - 20$', width=15, font=("Helvetica", 12, "italic"),
                               variable=self.r, value=3).place(x=450, y=300)

        self.img1 = PhotoImage(file='Extensions/pizzaSlices (2).gif')
        self.label_img1 = Label(master, image=self.img1).place(x=25, y=75)

        self.img2 = PhotoImage(file='Extensions/pizzaSlices (3).gif')
        self.label_img2 = Label(master, image=self.img2).place(x=200, y=50)

        self.img3 = PhotoImage(file='Extensions/pizzaSlices (4).gif')
        self.label_img3 = Label(master, image=self.img3).place(x=450, y=25)

        self.b1 = Button(self.master, text="Select", width=20, bg='MistyRose3', fg='white', command = self.size).place(x = 300, y=400)
        self.b2 = Button(self.master, text='Back', width=20, bg='MistyRose3', fg='white', command = self.cancel).place(x=300, y=450)
        self.b3 = Button(self.master, text='Quit', width=20, bg='MistyRose3', fg='white', command=self.master.quit).place(x=300, y=500)

    def size(self):

        #self.master.quit()
        var = self.r.get()

        if var == 1:
            self.pizza_size = 'Small'
            self.MyPizza = PizzaBuilder('Small')

        elif var == 2:
            self.pizza_size = 'Medium'
            self.MyPizza = PizzaBuilder('Medium')

        elif var == 3:
            self.pizza_size = 'Large'
            self.MyPizza = PizzaBuilder('Large')

        #print(self.pizza_size)

        c = Toplevel(self.master)
        cc = Custom(c, self.name, self.MyPizza, self.order_id, self.master)
        self.master.withdraw()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.master.destroy()

class Custom:

    def __init__(self, master, name, mypizza, order_id, prev):

        self.order = []
        self.master = master
        self.master.geometry('900x550')
        self.master.title('Customize your pizza')
        self.name = name
        self.MyPizza = mypizza
        self.order_id = order_id
        self.prev = prev

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()

        self.c1 = Checkbutton(master, text="Tomato - 5$", variable=self.var1, font=("Helvetica", 12, "italic"),
                              width=15).place(x=25, y=150)
        self.c2 = Checkbutton(master, text="Mushroom - 4$", variable=self.var2, font=("Helvetica", 12, "italic"),
                              width=15).place(x=250, y=150)
        self.c3 = Checkbutton(master, text="Black olive - 4$", variable=self.var3, font=("Helvetica", 12, "italic"),
                              width=12).place(x=475, y=150)
        self.c4 = Checkbutton(master, text="Pepper - 5$", variable=self.var4, font=("Helvetica", 12, "italic"),
                              width=12).place(x=700, y=150)
        self.c5 = Checkbutton(master, text="Pepperoni - 7.5$", variable=self.var5, font=("Helvetica", 12, "italic"),
                              width=18).place(x=25, y=350)
        self.c6 = Checkbutton(master, text="Chicken - 8$", variable=self.var6, font=("Helvetica", 12, "italic"),
                              width=15).place(x=250, y=350)
        self.c7 = Checkbutton(master, text="Tuna - 9$", variable=self.var7, font=("Helvetica", 12, "italic"),
                              width=12).place(x=475, y=350)
        self.c8 = Checkbutton(master, text="Spinach - 3$", variable=self.var8, font=("Helvetica", 12, "italic"),
                              width=12).place(x=700, y=350)

        self.ext1 = PhotoImage(file='Extensions/tomato_gif.gif')
        self.label_img1 = Label(master, image=self.ext1).place(x=25, y=25)

        self.ext2 = PhotoImage(file='Extensions/mushroom_gif.gif')
        self.label_img2 = Label(master, image=self.ext2).place(x=250, y=25)

        self.ext3 = PhotoImage(file='Extensions/black_olive.gif')
        self.label_img3 = Label(master, image=self.ext3).place(x=475, y=25)

        self.ext4 = PhotoImage(file='Extensions/pepper_gif.gif')
        self.label_img4 = Label(master, image=self.ext4).place(x=700, y=25)

        self.ext5 = PhotoImage(file='Extensions/pepperoni_gif.gif')
        self.label_img5 = Label(master, image=self.ext5).place(x=25, y=225)

        self.ext6 = PhotoImage(file='Extensions/chicken_gif.gif')
        self.label_img6 = Label(master, image=self.ext6).place(x=250, y=225)

        self.ext7 = PhotoImage(file='Extensions/tuna_fish_gif.gif')
        self.label_img7 = Label(master, image=self.ext7).place(x=475, y=225)

        self.ext8 = PhotoImage(file='Extensions/spinach_gif.gif')
        self.label_img8 = Label(master, image=self.ext8).place(x=700, y=225)

        self.b1 = Button(master, text="Create", width=20, bg='MistyRose3', fg='white', command=self.items).place(x=360, y=400)
        self.b2 = Button(self.master, text='Back', width=20, bg='MistyRose3', fg='white', command = self.cancel).place(x=360, y=450)
        self.b3 = Button(self.master, text='Quit', width=20, bg='MistyRose3', fg='white', command=self.master.quit).place(x=360, y=500)

    def items(self):

        #self.master.quit()
        v1 = self.var1.get()
        v2 = self.var2.get()
        v3 = self.var3.get()
        v4 = self.var4.get()
        v5 = self.var5.get()
        v6 = self.var6.get()
        v7 = self.var7.get()
        v8 = self.var8.get()

        if v1 == 1:
            self.order.append('Tomato')
            self.MyPizza.add_extension('Tomato')

        if v2 == 1:
            self.order.append('Mushroom')
            self.MyPizza.add_extension('Mushroom')

        if v3 == 1:
            self.order.append('Black Olive')
            self.MyPizza.add_extension('Black_olive')

        if v4 == 1:
            self.order.append('Pepper')
            self.MyPizza.add_extension('Pepper')

        if v5 == 1:
            self.order.append('Pepperoni')
            self.MyPizza.add_extension('Pepperoni')

        if v6 == 1:
            self.order.append('Chicken')
            self.MyPizza.add_extension('Chicken')

        if v7 == 1:
            self.order.append('Tuna')
            self.MyPizza.add_extension('Tuna')

        if v8 == 1:
            self.order.append('Spinach')
            self.MyPizza.add_extension('Spinach')

        #for i in self.order:
        #    print(i)

        con = sqlite3.connect('Users.db')
        cursor = con.cursor()
        cursor.execute('INSERT INTO User_orders(Username, Order_id) VALUES (?, ?)', (self.name, self.order_id))
        cursor.execute('INSERT INTO Orders(Order_id, Order_content, History, Price) VALUES (?, ?, ?, ?)', (self.order_id, self.MyPizza.get_status(), datetime.datetime.now(), self.MyPizza.get_price()))
        con.commit()
        tkinter.messagebox.showinfo('Info', 'Your submission has been received.')
        self.master.destroy()
        self.prev.update()
        self.prev.deiconify()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.master.destroy()
