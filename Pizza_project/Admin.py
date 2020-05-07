from tkinter import *
import tkinter.messagebox
import sqlite3

class Admin_login:

    def __init__(self, root, prev):

        self.root = root
        self.root.geometry('500x500')
        self.root.title('Admin')
        self.prev = prev

        self.username = StringVar()
        self.password = StringVar()

        self.label_0 = Label(self.root, text="Login as admin", width=20, font=("bold", 20), fg='AntiqueWhite3')
        self.label_0.place(x=75, y=50)

        self.label_1 = Label(self.root, text='Username', width=10, font=("Helvetica", 12, "italic"), fg='LavenderBlush4')
        self.label_1.place(x=15, y=120)

        self.entry_1 = Entry(self.root, text=self.username, font=("Helvetica", 10))  # text
        self.entry_1.place(x=150, y=124, width=200)

        self.label_2 = Label(self.root, text='Password', width=10, font=("Helvetica", 12, "italic"), fg='LavenderBlush4')
        self.label_2.place(x=12, y=180)

        self.entry_2 = Entry(self.root, text=self.password, show='*', font=("Helvetica", 10))  # text
        self.entry_2.place(x=200, y=184, width=150)

        self.b1 = Button(self.root, text='Enter', width=20, bg='MistyRose3', fg='white', command=self.login).place(x=150, y=250)
        self.b2 = Button(self.root, text="Cancel", width=20, bg='MistyRose3', fg='white', command=self.cancel).place(x=150, y=320)

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.withdraw()

    def login(self):
        u = self.username.get()
        p = self.password.get()
        u1 = Admin.get_name()
        p1 = Admin.get_passw()
        if u == u1 and p == p1:
            x = Toplevel(self.root)
            xx = Admin(x, self.root)
            self.root.withdraw()
        else:
            tkinter.messagebox.showwarning('Warning', 'Please enter the correct username and password! ')


class Admin:

    __admin_name = 'Admin2020'
    __admin_password = '20thisisadmin20'
    pizzaas = []

    def __init__(self, root, prev):

        self.root = root
        self.root.geometry("500x500")
        self.root.title("Admin")
        self.prev = prev

        self.b1 = Button(self.root, text='Add pizza', width=20, bg='MistyRose3', fg='white', command = self.add_p).place(x=150, y=100)
        self.b2 = Button(self.root, text='Remove pizza', width=20, bg='MistyRose3', fg='white', command = self.remove_p).place(x=150, y=150)
        #self.b3 = Button(self.root, text='View menu', width=20, bg='MistyRose3', fg='white').place(x=150, y=200)
        self.b4 = Button(self.root, text='Log out', width=20, bg='MistyRose3', fg='white', command = self.cancel).place(x=150, y=250)

    @classmethod
    def get_name(cls):
        return cls.__admin_name

    @classmethod
    def get_passw(cls):
        return cls.__admin_password

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.withdraw()

    def add_p(self):
        a = Toplevel(self.root)
        b = Add_pizza(a, self.root)
        self.root.withdraw()

    def remove_p(self):
        a = Toplevel(self.root)
        b = Remove_pizza(a, self.root)
        self.root.withdraw()

class Add_pizza:

    def __init__(self, root, prev):

        self.root = root
        self.root.geometry('500x500')
        self.root.title('Add pizza')
        self.prev = prev

        self.p_name = StringVar()
        self.p_ingr = StringVar()
        self.pr = StringVar()

        self.label_0 = Label(self.root, text="Add new pizza", width=20, font=("bold", 20), fg='AntiqueWhite3')
        self.label_0.place(x=75, y=50)

        self.label_1 = Label(self.root, text='Pizza name', width=10, font=("Helvetica", 12, "italic"), fg='LavenderBlush4')
        self.label_1.place(x=15, y=120)

        self.entry_1 = Entry(self.root, text=self.p_name, font=("Helvetica", 10))  # text
        self.entry_1.place(x=150, y=124, width=200)

        self.label_2 = Label(self.root, text='Ingredients', width=10, font=("Helvetica", 12, "italic"), fg='LavenderBlush4')
        self.label_2.place(x=12, y=180)

        self.entry_2 = Entry(self.root, text=self.p_ingr, font=("Helvetica", 10))  # text
        self.entry_2.place(x=150, y=184, width=200)

        self.label_3 = Label(self.root, text='Price', width=10, font=("Helvetica", 12, "italic"), fg='LavenderBlush4')
        self.label_3.place(x=15, y=240)

        self.entry_3 = Entry(self.root, text=self.pr, font=("Helvetica", 10))  # text
        self.entry_3.place(x=150, y=244, width=200)

        self.b1 = Button(self.root, text="Add", width=20, bg='MistyRose3', fg='white', command = self.add).place(x = 170, y=300)
        self.b2 = Button(self.root, text='Back', width=20, bg='MistyRose3', fg='white', command = self.cancel).place(x=170, y=350)
        self.b3 = Button(self.root, text='Quit', width=20, bg='MistyRose3', fg='white', command=self.root.quit).place(x=170, y=400)

    def add(self):

        n = self.p_name.get()
        i = self.p_ingr.get()
        p = self.pr.get()

        con = sqlite3.connect('Pizzeria.db')
        cursor = con.cursor()
        cursor.execute('SELECT Pizza_id FROM Pizzas WHERE Pizza_id = (SELECT MAX(Pizza_id) FROM Pizzas)')
        pizza_id = cursor.fetchone()[0] + 1

        cursor.execute('INSERT INTO Pizzas (Pizza, Pizza_id, Ingredients, Price) VALUES (?, ?, ?, ?)', (n, pizza_id, i, p))
        Admin.pizzaas.append(n)
        con.commit()
        con.close()
        tkinter.messagebox.showinfo('Info', 'New pizza has been added to menu. ')
        self.root.destroy()
        self.prev.update()
        self.prev.deiconify()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.withdraw()

class Remove_pizza:

    def __init__(self, root, prev):

        self.root = root
        root.geometry('500x800')
        root.title('Remove Pizza')
        self.prev = prev

        self.r = IntVar()

        con = sqlite3.connect('Pizzeria.db')
        cursor = con.cursor()
        cursor.execute('SELECT Pizza_id FROM Pizzas WHERE Pizza_id = (SELECT MAX(Pizza_id) FROM Pizzas)')
        id = cursor.fetchall()[0][0]
        #print(id)

        if id > 6:
            h = 20
            cursor.execute('SELECT Pizza FROM Pizzas WHERE Pizza_id > ?', (6, ))
            pza = cursor.fetchall()
            #print(pza)
            n = len(pza)
            for i in range(0, n):
                Radiobutton(root, text=pza[i][0], width=15, font=("Helvetica", 12, "italic"), variable=self.r, value=id+i).place(x=10, y=100 + h)
                h += 50

        else:
            tkinter.messagebox.showwarning('Warning', 'No pizzas to remove. ')

        con.close()
        self.b1 = Button(self.root, text=" Remove", width=20, bg='MistyRose3', fg='white', command = self.rmv).place(x = 170, y=650)
        self.b2 = Button(self.root, text="Back", width=20, bg='MistyRose3', fg='white', command=self.cancel).place(x=170, y=700)
        self.b3 = Button(self.root, text="Quit", width=20, bg='MistyRose3', fg='white', command=self.root.quit).place(x=170, y=750)

    def rmv(self):
        var = self.r.get()
        if var == 0:
            self.prev.update()
            self.prev.deiconify()
            self.root.destroy()

        else:
            con = sqlite3.connect("Pizzeria.db")
            cursor = con.cursor()
            cursor.execute('DELETE FROM Pizzas WHERE Pizza_id = ?', (var, ))
            con.commit()
            con.close()
            tkinter.messagebox.showinfo('Info', 'Pizza has been deleted from menu. ')
            self.prev.update()
            self.prev.deiconify()
            self.root.destroy()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.withdraw()
