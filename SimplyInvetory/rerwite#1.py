import tkinter as tk
from tkinter import ttk
import os
import json
import requests
import base64
import mysql.connector

LARGE_FONT = ("Verdana", 12)
BACKGROUND = "white"
FOREGROUND = "black"

tcgplayer_url = "http://api.tcgplayer.com/v1.32.0/stores/7c2bc097/"
ship_station_url = "https://ssapi.shipstation.com/orders"

logedon = False

forms = []
entry_forms = []
global first_run
first_run = True
pagenumber = 1

class mysqlDatabase():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="SimplyUnlucky",
            passwd="459799Oo",
            database="SimplyUnlucky"
        )

        self.mycursor = self.mydb.cursor()

    def createDatabse(self, name):

        self.mycursor.execute("CRATE DATABASE " + name)

    def getInventory(self):
        
        inventory = []

        self.mycursor.execute("SELECT * FROM Inventory")

        myresult = self.mycursor.fetchall()

        return myresult

    def addToInvenotory(self, name, qty, table):
        print("INSERT INTO " + table + "(name, qty) VALUES ('" + name + "','" + qty + "');")
        self.mycursor.execute("INSERT INTO " + table + "(name, qtr) VALUES ('" + name + "','" + qty + "');")

    def get_table(self,search,table):
        self.mycursor.execute("SELECT " + str(search) + " FROM " + str(table))

        return self.mycursor.fetchall()

class shipstation():

    def add_order(self, *args, **kwargs):
        print(kwargs.get("orderNumber", None))


    def get_orders(self):
        
        auth = base64.b64encode("4b42163a2344409780dca83c93aac587:a7bc884a9a60406da98ef7bb5de978c8".encode('utf-8'))
        
        headers = {
            'Authorization': 'Basic ' + auth.decode("utf-8")
        }
        print(auth.decode("utf-8"))

        request = requests.get('https://ssapi.shipstation.com/orders?sortBy=OrderDate&sortDir=DESC', headers=headers)

        if request.status_code == "401":
            print("AWWWW FUCK")
            return

        order = request.json()

        return order

def removeOrders():
    for i in range(len(forms)):
        for x in range(len(forms[i])):
            print(forms[i][x])
            forms[i][x].delete(0, tk.END)

def add_page(pagenumber, order_canvas):
    pagenumber = pagenumber + 1
    #removeOrders()
    draw_orders(order_canvas,pagenumber,vsb)

def minus_page(pagenumber, order_canvas):
    pagenumber = pagenumber - 1
    #removeOrders()
    draw_orders(order_canvas,pagenumber,vsb)

def draw_orders(frame, pagenumber):
    test = db.get_table("*","Orders")
    count = 0
    forms_frame = tk.Frame(frame)
    print(test[1])
    print((50*pagenumber)-50, 50*pagenumber)
    #print(first_run)
    for i in range((50*pagenumber)-50, 50*pagenumber):
        count = count + 1
        entry_forms = []

        try:
            name_texting = test[i+pagenumber][1]
            #print(name_texting)
            name = tk.Entry(forms_frame)
            try:
                name.insert(0, name_texting)
            except NameError:
                name.insert(0, "Error")
            entry_forms.append(name)

            date_text = test[i][2]
            #print(date_text)
            date = tk.Entry(forms_frame)
            try:
                date.insert(0, date_text)
            except NameError:
                date.insert(0, "Error")
            entry_forms.append(date)

            billto_text = test[i][3]
            #print(billto_text)
            billto = tk.Entry(forms_frame)
            try:
                billto.insert(0, billto_text)
            except NameError:
                billto.insert(0, "Error")
            entry_forms.append(billto)

            adress_text = test[i][4]
            #print(adress_text)
            adress = tk.Entry(forms_frame)
            try:
                adress.insert(0, adress_text)
            except NameError:
                adress.insert(0, "Error")
            entry_forms.append(adress)

            item1_text = test[i][5]
            #print(adress_text)
            item1 = tk.Entry(forms_frame,  width=80)
            try:
                item1.insert(0, item1_text)
            except NameError:
                item1.insert(0, "Error")
            entry_forms.append(item1)

            #qty_text = test[i][6]
            #print(qty_text)
            #qty = tk.Entry(frame)
            #try:
            #    qty.insert(0, qty_text)
            #except NameError:
            #    qty.insert(0, "Error")
            #entry_forms.append(qty)

            #try:
            #    if test["orders"][i]["items"][1]["name"] != None:

            #        item_id = test["orders"][i]["orderId"]

            #        multiple = tk.Button(frame, text="Multiple Item", command = lambda: expand(item_id))

            #        entry_forms.append(multiple)
            #except:
            #    pass
 
            forms.append(entry_forms)

        except ValueError:
            continue

        for i in range(i):

            print((50*pagenumber)-50, 50*pagenumber)
            print(forms[i])
            for x in range(len(forms[i])):
                forms[i][x].grid(row=i, column=x)

    forms_frame.pack()
    frame.config(yscrollcommand=vsb.set, scrollregion=(0,0,1200,1000))
def draw_login_screen():

    def check_creds(root, username, password):

        if username == "SimplyUnlucky" and password == "ez":
            root.destroy()
        else:
            draw_login_screen()

    screen_frame = tk.Tk()

    screen_frame.geometry("300x100")

    username = tk.Entry(screen_frame, text="Username")
    password = tk.Entry(screen_frame, text="Password")
    login_button = tk.Button(screen_frame, text='Login', command=lambda: check_creds(screen_frame, username.get(), password.get()))

    username.pack()
    password.pack()
    login_button.pack()

    screen_frame.mainloop()

def draw_main_screen():

    root = tk.Tk()

    root.geometry("1200x1000")

    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Load")
    filemenu.add_command(label="Save")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Orders")
    helpmenu.add_command(label="About...")
    menubar.add_cascade(label="Sync", menu=helpmenu)

    root.config(menu=menubar)

    tabControl = ttk.Notebook(root)

    Tab1 = ttk.Frame(tabControl)
    Tab2 = ttk.Frame(tabControl)
    Tab3 = ttk.Frame(tabControl)
    Tab4 = ttk.Frame(tabControl)

    tabControl.add(Tab1, text="Orders")
    tabControl.add(Tab2, text="Inventory")
    tabControl.add(Tab3, text="Orders")
    tabControl.add(Tab4, text="Out of stock")
    tabControl.pack(expand = True, fill="both")

    orders_canvas = tk.Canvas(Tab1, width=150, height=150)
    vsb = tk.Scrollbar(Tab1,orient='vertical', command=orders_canvas.yview)
    orders_canvas.config(yscrollcommand=vsb.set, scrollregion=(0,0,1200,1000))
    vsb.grid(row=1, column=2, sticky="ns")
    draw_orders(orders_canvas,pagenumber)
    orders_canvas.grid(row=1, column=1)

    button_frame = tk.Frame(Tab1)
    button_frame.grid(row=2, column=1)

    next_page_button = tk.Button(button_frame, text="Next Page", command=lambda: add_page(pagenumber, orders_canvas))
    prev_page_button = tk.Button(button_frame, text="Prev Page", command=lambda: minus_page(pagenumber, orders_canvas))

    next_page_button.grid(row=1, column=1)
    prev_page_button.grid(row=1, column=0)

    root.mainloop()

sp = shipstation()
db = mysqlDatabase()
draw_login_screen()
draw_main_screen()
