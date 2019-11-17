import base64
import requests
import tkinter as tk
from tkinter import ttk
import json

LARGE_FONT = ("Verdana", 12)
BACKGROUND = "white"
FOREGROUND = "black"

tcgplayer_url = "http://api.tcgplayer.com/v1.32.0/stores/7c2bc097/"
ship_station_url = "https://ssapi.shipstation.com/orders"

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
    entry_forms = []
    
    name_forms = []
    date_form = []

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

        tabControl.add(Tab1, text="HOT!!!")
        tabControl.add(Tab2, text="Inventory")
        tabControl.add(Tab3, text="Orders")
        tabControl.add(Tab4, text="Out of stock")
        tabControl.pack(expand = 1, fill="both")

        test = sp.get_orders()
        page = 1

        def draw_forms(page_number):

            for i in range(len(self.forms)):
                self.forms[i] = None

            for i in range(page_number*50):

                #print(test["orders"][i]["shipTo"]["city"])

                entry_forms = []

                try:
                    name_texting = test["orders"][i]["orderId"]
                    print(name_texting)
                    name = tk.Entry(Tab1)
                    try:
                        name.insert(0, name_texting)
                    except NameError:
                        name.insert(0, "Error")
                    entry_forms.append(name)

                    date_text = test["orders"][i]["orderDate"]
                    print(date_text)
                    date = tk.Entry(Tab1)
                    try:
                        date.insert(0, date_text)
                    except NameError:
                        date.insert(0, "Error")
                    entry_forms.append(date)

                    billto_text = test["orders"][i]["shipTo"]["city"]
                    print(billto_text)
                    billto = tk.Entry(Tab1)
                    try:
                        billto.insert(0, billto_text)
                    except NameError:
                        billto.insert(0, "Error")
                    entry_forms.append(billto)

                    
                    adress_text = test["orders"][i]["shipTo"]["street1"]
                    print(adress_text)
                    adress = tk.Entry(Tab1)
                    try:
                        adress.insert(0, adress_text)
                    except NameError:
                        adress.insert(0, "Error")
                    entry_forms.append(adress)

                    item1_text = test["orders"][i]["items"][0]["name"]
                    print(adress_text)
                    item1 = tk.Entry(Tab1,  width=80)
                    try:
                        item1.insert(0, item1_text)
                    except NameError:
                        item1.insert(0, "Error")
                    entry_forms.append(item1)

                    qty_text = test["orders"][i]["items"][0]["quantity"]
                    print(qty_text)
                    qty = tk.Entry(Tab1)
                    try:
                        qty.insert(0, qty_text)
                    except NameError:
                        qty.insert(0, "Error")
                    entry_forms.append(qty)

                    price_text = test["orders"][i]["items"][0]["unitPrice"]
                    print(price_text)
                    price = tk.Entry(Tab1)
                    try:
                        qty.insert(0, price_text)
                    except NameError:
                        qty.insert(0, "Error")
                    entry_forms.append(price)

                    self.forms.append(entry_forms)
                except KeyError:
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

        def change_page(page_number_1s):
            
            page_number_1s = page_number_1s + 1

            draw_forms(page)

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

tp = tcgplayer()
sp = shipstation()
app = ObjTkinter()
app.mainloop()