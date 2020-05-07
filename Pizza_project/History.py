from tkinter import *
import sqlite3

class History:

    def __init__(self, master, name, prev):

        self.master = master
        self.master.geometry('800x550')
        self.master.title('History')
        self.name = name
        self.prev = prev

        self.label_0 = Label(master, text=f"History of purchases: {self.name}", width=25, font=("bold", 20), fg='AntiqueWhite3').place(x = 200, y = 25)
        self.label_1 = Label(master, text= "Purchase", width=20, font=("bold", 15), fg='AntiqueWhite3').place(x = 50, y = 75)
        self.label_2 = Label(master, text= "Price", width=20, font=("bold", 15), fg='AntiqueWhite3').place(x = 260, y = 75)
        self.label_3 = Label(master, text= "Date and time", width=25, font=("bold", 15), fg='AntiqueWhite3').place(x = 400, y = 75)
        self.date_time = Listbox(master, width = 28, height = 20)
        self.cost = Listbox(master, width = 8, height = 20)
        self.items = Listbox(master, width = 40, height = 20)

        self.b1 = Button(self.master, text='Back', width=20, bg='MistyRose3', fg='white', command=self.cancel).place(x=250, y=450)
        self.b2 = Button(self.master, text='Quit', width=20, bg='MistyRose3', fg='white', command=self.master.quit).place(x=250, y=500)

    def func(self):
        con = sqlite3.connect('Users.db')
        cursor = con.cursor()
        cursor.execute('SELECT Order_id FROM User_orders WHERE Username = ?', (self.name, ))
        ids = cursor.fetchall()
        n = len(ids)
        #print(self.name)

        hist = []
        pr = []
        ing = []
        for i in ids:
            cursor.execute('SELECT History FROM Orders WHERE Order_id = ?', (i[0], ))
            h = cursor.fetchone()
            hist.append(h)

            cursor.execute('SELECT Price FROM Orders WHERE Order_id = ?', (i[0], ))
            p = cursor.fetchone()
            pr.append(p)

            cursor.execute('SELECT Order_content FROM Orders WHERE Order_id = ?', (i[0],))
            item = cursor.fetchone()
            ing.append(item)

        #print(ids)
        #print(hist)
        #print(pr)
        #print(ing)

        self.cost.insert(END, *pr)
        self.cost.place(x=350, y=100)
        self.date_time.insert(END, *hist)
        self.date_time.place(x=450, y=100)
        self.items.insert(END, *ing)
        self.items.place(x = 50, y = 100)

    def cancel(self):
        self.prev.update()
        self.prev.deiconify()
        self.master.destroy()

'''if __name__ == "__main__":

    root  = Tk()
    r = History(root, 'User9')
    r.func()
    root.mainloop()'''