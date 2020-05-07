import sqlite3
con = sqlite3.connect('Users.db')
cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS User_orders (Username TEXT, Order_id REAL)')
cursor.execute('CREATE TABLE IF NOT EXISTS Orders (Order_id REAL, Order_content TEXT, History Text, Price TEXT)')

#cursor.execute('INSERT INTO User_orders(Username, Order_id) VALUES (?, ?)', ('None', 0))
#cursor.execute('INSERT INTO Orders(Order_id, Order_content, History, Price) VALUES (?, ?, ?, ?)', (0, 'None', 'None', 'None'))

con.commit()
con.close()

con = sqlite3.connect('Pizzeria.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Pizzas (Pizza TEXT, Pizza_id REAL, Ingredients TEXT, Price TEXT)')

'''cursor.execute('INSERT INTO Pizzas (Pizza, Pizza_id, Ingredients, Price) VALUES (?, ?, ?, ?)', ('Margherita Pizza', 1, 'Tomato Mozarella Chicken',35))
cursor.execute('INSERT INTO Pizzas (Pizza, Pizza_id, Ingredients, Price) VALUES (?, ?, ?, ?)', ('Hawaiian Pizza', 2, 'Tomato Mozarella Pineapple',45))
cursor.execute('INSERT INTO Pizzas (Pizza, Pizza_id, Ingredients, Price) VALUES (?, ?, ?, ?)', ('Sicilian Pizza', 3, 'Tomato Mozarella, Onion',45))
cursor.execute('INSERT INTO Pizzas (Pizza, Pizza_id, Ingredients, Price) VALUES (?, ?, ?, ?)', ('Pizza Vegetariana', 4, 'Tomato Pepper Spinach',30))
cursor.execute('INSERT INTO Pizzas (Pizza, Pizza_id, Ingredients, Price) VALUES (?, ?, ?, ?)', ('Mexican Taco Pizza', 5, 'Tomato Pepper Black olive',65))
cursor.execute('INSERT INTO Pizzas (Pizza, Pizza_id, Ingredients, Price) VALUES (?, ?, ?, ?)', ('Pizza Deluxe', 6, 'Pepperoni Tomato, Pepper',50))'''

con.commit()
con.close()