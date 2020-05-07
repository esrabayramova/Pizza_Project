import sqlite3
import tkinter.messagebox
from tkinter import *
from Profile import Order, Custom, Custom_size, Menu
from History import History
from Admin import Admin, Admin_login

con = sqlite3.connect('Users.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS LoginInfo (Username TEXT, Password TEXT)')
cursor.execute('SELECT Username FROM LoginInfo')
names = cursor.fetchall()
n = len(names)
arr = []
#print(names)
#print(n)

if len(names) == 0:
    #print(None)
    pass
else:
    for i in range(0, n):
        arr.append(names[i][0])

#print(arr)

class SignUp:

    def __init__(self, root, prev):

        self.root = root
        self.prev = prev
        self.root.geometry('500x500')
        self.root.title('Sign Up')

        self.username = StringVar()
        self.a = StringVar()
        self.b = StringVar()

        self.label_0 = Label(self.root, text="SignUp", width=20, font=("bold", 20), fg='AntiqueWhite3')
        self.label_0.place(x=75, y=50)

        self.label_1 = Label(self.root, text='Username', width=10, font=("Helvetica", 12, "italic"),
                             fg='LavenderBlush4')
        self.label_1.place(x=15, y=120)

        self.entry_1 = Entry(self.root, text=self.username, font=("Helvetica", 10))
        self.entry_1.place(x=150, y=124, width=200)

        self.label_2 = Label(self.root, text='Password', width=10, font=("Helvetica", 12, "italic"),
                             fg='LavenderBlush4')
        self.label_2.place(x=12, y=180)

        self.entry_2 = Entry(self.root, text=self.a, show='*', font=("Helvetica", 10))
        self.entry_2.place(x=200, y=184, width=150)

        self.label_3 = Label(self.root, text="Confirm Password", width=15, font=("Helvetica", 12, "italic"),
                             fg='LavenderBlush4')
        self.label_3.place(x=12, y=235)

        self.entry_3 = Entry(self.root, text=self.b, show='*', font=("Helvetica", 10))
        self.entry_3.place(x=200, y=240, width=150)

        self.b1 = Button(self.root, text='Create Profile', width=20, bg='MistyRose3', fg='white', command=self.flag).place(x=150, y=350)
        self.b2 = Button(self.root, text="Cancel", width=20, bg='MistyRose3', fg='white', command=self.cancel).place(x=150, y=400)

    def flag(self):

        con = sqlite3.connect("Users.db")
        cursor = con.cursor()

        username1 = self.username.get()
        password1 = self.a.get()
        password2 = self.b.get()

        username_available = True
        confirm_password = True

        if len(password2) == 0 or len(password1) == 0:
            confirm_password = False
        else:
            confirm_password = (password1 == password2)

        if len(username1) == 0:
            username_available = False
        else:
            cursor.execute("SELECT Username FROM LoginInfo")
            rows = cursor.fetchall()
            for row in rows:
                if row[0] == username1:
                    username_available = False
                    break

        if username_available == False:
            if len(username1) == 0:
                tkinter.messagebox.showwarning("Blank", 'Make sure to fill in the blanks.')
            else:
                tkinter.messagebox.showwarning('Warning', "This username is already taken. ")

        else:
            if confirm_password == False:
                if len(password2) == 0 or len(password1) == 0:
                    tkinter.messagebox.showwarning("Blank", 'Make sure to fill in the blanks.')
                else:
                    tkinter.messagebox.showerror('Error', "Those passwords didn`t match. Try again.")
            else:
                cursor.execute("INSERT INTO LoginInfo(Username, Password) VALUES (?, ?)", (username1, password1))
                arr.append(username1)
                con.commit()
                tkinter.messagebox.showinfo("Info", 'Account created.')
                self.prev.update()
                self.prev.deiconify()
                self.root.destroy()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.destroy()

class SignIn:

    def __init__(self, root, prev):

        self.root = root
        self.root.geometry('500x500')
        self.root.title('Sign in')
        self.prev = prev

        self.username = StringVar()
        self.password = StringVar()

        self.label_0 = Label(self.root, text="SignIn", width=20, font=("bold", 20), fg='AntiqueWhite3')
        self.label_0.place(x=75, y=50)

        self.label_1 = Label(self.root, text='Username', width=10, font=("Helvetica", 12, "italic"), fg='LavenderBlush4')
        self.label_1.place(x=15, y=120)

        self.entry_1 = Entry(self.root, text=self.username, font=("Helvetica", 10))  # text
        self.entry_1.place(x=150, y=124, width=200)

        self.label_2 = Label(self.root, text='Password', width=10, font=("Helvetica", 12, "italic"), fg='LavenderBlush4')
        self.label_2.place(x=12, y=180)

        self.entry_2 = Entry(self.root, text=self.password, show='*', font=("Helvetica", 10))  # text
        self.entry_2.place(x=200, y=184, width=150)

        self.b1 = Button(self.root, text='Enter', width=20, bg='MistyRose3', fg='white', command=self.profile).place(x=150, y=250)
        self.b2 = Button(self.root, text="Cancel", width=20, bg='MistyRose3', fg='white', command=self.cancel).place(x=150, y=320)

    def profile(self):

        username1 = self.username.get()
        password1 = self.password.get()

        con = sqlite3.connect("Users.db")
        cursor = con.cursor()

        if len(username1) == 0:
            tkinter.messagebox.showwarning("Warning", 'Please enter the username')
        elif len(password1) == 0:
            tkinter.messagebox.showwarning('Warning', 'Please enter the password')
        elif username1 not in arr:
            tkinter.messagebox.showwarning("Mismatched", 'Username and password did not match. Try again!')
        else:
            cursor.execute("SELECT Password FROM LoginInfo WHERE Username=?", (username1, ))
            p = cursor.fetchone()
            if password1 != p[0]:
                tkinter.messagebox.showwarning("Mismatched", 'Username and password did not match. Try again!')
                #print(p[0])
            else:
                p = Toplevel(self.root)
                profile = MyProfile(p, username1, self.root)
                self.root.withdraw()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.destroy()

class MyProfile:

    def __init__(self, root, name, prev):

        self.root = root
        self.root.geometry('500x400')
        self.root.title('My profile')
        self.name = name
        self.prev = prev

        self.name_label = Label(self.root, text=f"Welcome, {self.name}", width=20, font=("bold", 20), fg='AntiqueWhite3').place(x = 50, y = 60)
        self.b1 = Button(self.root, text='Order pizza', width=20, bg='MistyRose3', fg='white', command = self.pizza_order).place(x=150, y=150)
        self.b2 = Button(self.root, text='View history', width=20, bg='MistyRose3', fg='white', command = self.histo).place(x=150, y=200)
        self.b3 = Button(self.root, text='Log out', width=20, bg='MistyRose3', fg='white', command = self.cancel).place(x=150, y=250)

    def pizza_order(self):
        pz = Toplevel(self.root)
        pizza = Order(pz, self.name, self.root)
        self.root.withdraw()

    def histo(self):
        hi = Toplevel(self.root)
        hist = History(hi, self.name, self.root)
        hist.func()
        self.root.withdraw()

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.root.destroy()

class MainMenu:

    def __init__(self, root):

        self.root = root
        self.root.geometry('450x750')
        self.root.title('Main menu')

        self.logo = PhotoImage(file = 'pizzeria_logo.gif')
        self.label_logo = Label(root, image=self.logo).place(x=0, y=0)

        self.b1 = Button(self.root, text='Sign in', width=20, bg='MistyRose3', fg='white', command = self.sign_in).place(x=150, y=600)
        self.b2 = Button(self.root, text='Sign up', width=20, bg='MistyRose3', fg='white', command = self.sign_up).place(x=150, y=650)
        self.b3 = Button(self.root, text='Login as admin', width=20, bg='MistyRose3', fg='white', command = self.admin_login).place(x=150, y=700)
        #self.b4 = Button(self.root, text='Close', width=20, bg='MistyRose3', fg='white', command = self.root.quit).place(x=150, y=750)

    def sign_in(self):
        root1 = Toplevel(self.root)
        signin = SignIn(root1, self.root)
        #self.root.deiconify()
        self.root.withdraw()

    def sign_up(self):
        root2 = Toplevel(self.root)
        signup = SignUp(root2, self.root)
        #self.root.deiconify()
        self.root.withdraw()

    def admin_login(self):
        root3 = Toplevel(self.root)
        login = Admin_login(root3, self.root)
        self.root.withdraw()
