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


test = ['{ "name":"John", "qty":30, "selling":15}','{ "name":"Ryan", "qty":30, "selling":15}','{ "name":"dsadsa", "qty":30, "selling":15}']

class ObjTkinter(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        
        mainFrame = tk.Frame(self)
        mainFrame.pack(side="top", fill="both", expand = True)

        mainFrame.grid_rowconfigure(0, weight=0)
        mainFrame.grid_columnconfigure(0, weight=0)
        self.title("SimplyHOT")

        self.frames = {}

        for F in (MainPage, loginPage):

            frame = F(mainFrame, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        #frame = MainPage(mainFrame, self)

        #self.frames[MainPage] = frame

        #frame.grid(row=0, column=0, sticky="nsew")

        # Delet this for new page ^

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):

    forms = []
    orders_forms = []
    inventory_forms = []
    entry_forms = []
    entry_forms2 = []
    name_forms = []
    date_form = []

    card_name_forms = []
    qty_forms = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=400, height=200, bg="white")

        tabControl = ttk.Notebook(self)

        Tab1 = ttk.Frame(tabControl)
        Tab2 = ttk.Frame(tabControl)
        Tab3 = ttk.Frame(tabControl)
        Tab4 = ttk.Frame(tabControl)

        #tk.Label(Tab1, text="Name").grid(row=0, column=1)
        #tk.Label(Tab1, text="test").grid(row=0, column=2)
        #tk.Label(Tab1, text="test2").grid(row=0, column=3)

        tabControl.add(Tab1, text="Orders")
        tabControl.add(Tab2, text="Inventory")
        tabControl.add(Tab3, text="Orders")
        tabControl.add(Tab4, text="Out of stock")
        tabControl.pack(expand = 1, fill="both")

        db.addToInvenotory("Test2","2", "Inventory")
        test = sp.get_orders()
        page = 1

        def draw_forms_for_inventory():

            for i in range(50):

                    try:
                        entry_forms2 = []
                        
                        inventory = db.getInventory()

                        name_of_card_text = inventory[i][0]
                        print(name_of_card_text)
                        name_of_card = tk.Entry(Tab2)
                        try:
                            name_of_card.insert(0, name_of_card_text)
                        except NameError:
                            name_of_card.insert(0, "Error")
                        entry_forms2.append(name_of_card)
                    except:
                        continue

                    try:
                        qty_text = inventory[i][1]
                        print(qty_text)
                        qty = tk.Entry(Tab2)
                        try:
                            qty.insert(0, qty_text)
                        except NameError:
                            qty.insert(0, "Error")
                        entry_forms2.append(qty)

                        self.inventory_forms.append(entry_forms2)

                        for i in range(len(self.inventory_forms)):
                                for x in range(len(self.inventory_forms[i])):
                                    self.inventory_forms[i][x].grid(row=i, column=x)
                    except:
                        continue


        def draw_forms_for_orders_from_shipstation(page_number):

            try:
                for i in range(len(self.forms)):
                    for x in range(len(self.forms[i])):
                        self.forms[i][x].destroy()
                
                #for i in range(len(self.forms)):

            except:
                pass

            for i in range(page_number*50):

                print("test")

                #print(test["orders"][i]["shipTo"]["city"])

                entry_forms = []

                try:
                    name_texting = test["orders"][i]["orderId"]
                    #print(name_texting)
                    name = tk.Entry(Tab1)
                    try:
                        name.insert(0, name_texting)
                    except NameError:
                        name.insert(0, "Error")
                    entry_forms.append(name)

                    date_text = test["orders"][i]["orderDate"]
                    #print(date_text)
                    date = tk.Entry(Tab1)
                    try:
                        date.insert(0, date_text)
                    except NameError:
                        date.insert(0, "Error")
                    entry_forms.append(date)

                    billto_text = test["orders"][i]["shipTo"]["city"]
                    #print(billto_text)
                    billto = tk.Entry(Tab1)
                    try:
                        billto.insert(0, billto_text)
                    except NameError:
                        billto.insert(0, "Error")
                    entry_forms.append(billto)

                    adress_text = test["orders"][i]["shipTo"]["street1"]
                    #print(adress_text)
                    adress = tk.Entry(Tab1)
                    try:
                        adress.insert(0, adress_text)
                    except NameError:
                        adress.insert(0, "Error")
                    entry_forms.append(adress)

                    item1_text = test["orders"][i]["items"][0]["name"]
                   #print(adress_text)
                    item1 = tk.Entry(Tab1,  width=80)
                    try:
                        item1.insert(0, item1_text)
                    except NameError:
                        item1.insert(0, "Error")
                    entry_forms.append(item1)

                    qty_text = test["orders"][i]["items"][0]["quantity"]
                    #print(qty_text)
                    qty = tk.Entry(Tab1)
                    try:
                        qty.insert(0, qty_text)
                    except NameError:
                        qty.insert(0, "Error")
                    entry_forms.append(qty)

                    price_text = test["orders"][i]["items"][0]["unitPrice"]
                    #print(price_text)
                    price = tk.Entry(Tab1)
                    try:
                        price.insert(0, price_text)
                    except NameError:
                        price.insert(0, "Error")
                    entry_forms.append(price)

                    try:
                        if test["orders"][i]["items"][1]["name"] != None:

                            item_id = test["orders"][i]["orderId"]

                            multiple = tk.Button(Tab1, text="Multiple Item", command = lambda: expand(item_id))
 
                            entry_forms.append(multiple)
                    except:
                        pass

                    self.forms.append(entry_forms)
                except NameError:
                    continue
                
                for i in range(len(self.forms)):
                    for x in range(len(self.forms[i])):
                        self.forms[i][x].grid(row=i, column=x)

            #entry_frames.append(tk.Frame(Tab1))
            #entry_frames[i].grid(row=i+1, column=1)

            #name_entry = orders["orders"][i]["orderNumber"]
            #form = tk.Entry(entry_frames[i])
            #names_forms.append(form)
            #names_forms[i].insert(0, name_entry)

            # Code to add a form to the frame
            #form2 = tk.Entry(entry_frames[i])
            #item_entry = orders["orders"][i]["items"]["sku"]
            #item_forms.append(form2)
            #item_forms[i].insert(0, item_entry)         
        #sp.add_order(orderNumber="1")

        def expand(num):
            print(num)

        def change_page(page_number_1s):
            
            page_number_1s = page_number_1s + 1
            draw_forms_for_orders_from_shipstation(page)

        draw_forms_for_inventory()
        draw_forms_for_orders_from_shipstation(page)

        page_up = tk.Button(Tab1, text="Next Page", command=lambda: change_page(page))
        page_up.grid(row=51, column=0)



class loginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=400, height=200, bg="white")
        
class tcgplayer():

    def get_orders(self, *args, **kwargs):
        request = requests.get(tcgplayer_url, headers=None)
        print(request.text)

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

#class ebay():
#    def get_sales(self):
#        auth = base64.b64encode("4b42163a2344409780dca83c93aac587:a7bc884a9a60406da98ef7bb5de978c8".encode('utf-8'))
        
#        headers = {
#            'Authorization': 'Basic ' + auth.decode("utf-8")
#        }
#        print(auth.decode("utf-8"))

#        request = requests.get('https://ssapi.shipstation.com/orders?sortBy=OrderDate&sortDir=DESC', headers=headers)

#        if request.status_code == "401":
#            print("AWWWW FUCK")
#            return

#        order = request.json()

#        return order

        


class mysqlDatabase():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="SimplyUnlucky",
            passwd="459799Oo",
            database="SimplyUnluck"
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



db = mysqlDatabase()
tp = tcgplayer()
sp = shipstation()
app = ObjTkinter()
app.mainloop()