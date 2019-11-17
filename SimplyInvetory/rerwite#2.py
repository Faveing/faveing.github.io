import tkinter as tk
from tkinter import ttk
import os
import json
import requests
import base64
import mysql.connector
import re

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

    def getOrders(self):

        orders = []

        self.mycursor.execute("SELECT * FROM Orders;")

        myresult = self.mycursor.fetchall()

        return myresult

    def getInventory(self):
        
        inventory = []

        self.mycursor.execute("SELECT * FROM Inventory;")

        myresult = self.mycursor.fetchall()

        return myresult

    def getRowFromInventory(self, num):

        inventory = []

        num = num - 1

        self.mycursor.execute("SELECT * FROM Inventory LIMIT " + str(num) + ",1")

        myresult = self.mycursor.fetchall()

        return myresult

    def updateRow(self,sku,name,qty,quality,rare,selling,location,tcgplayer,ebayprice,cat):

        if sku != None:
            if name != "":
                self.mycursor.execute("UPDATE Inventory SET name='" + name + "' WHERE Sku = '" + sku + "';")
                print("Updated name of" + sku)
            if qty != "":
                self.mycursor.execute("UPDATE Inventory SET qty='" + qty + "' WHERE Sku = '" + sku + "';")
                print("Updated qty of" + sku)
            if quality != "":
                self.mycursor.execute("UPDATE Inventory SET quality='" + quality + "' WHERE Sku = '" + sku + "';")
                print("Updated quality of" + sku)
            if rare != "":
                self.mycursor.execute("UPDATE Inventory SET rare='" + rare + "' WHERE Sku = '" + sku + "';")
                print("Updated rare of" + sku)
            if selling != "":
                self.mycursor.execute("UPDATE Inventory SET selling='" + selling + "' WHERE Sku = '" + sku + "';")
                print("Updated selling of" + sku)
            if location != "":
                self.mycursor.execute("UPDATE Inventory SET location='" + location + "' WHERE Sku = '" + sku + "';")
                print("Updated location of" + sku)
            if tcgplayer != "":
                self.mycursor.execute("UPDATE Inventory SET TCGPrice='" + tcgplayer + "' WHERE Sku = '" + sku + "';")
                print("Updated tcgplayer of" + sku)
            if ebayprice != "":
                self.mycursor.execute("UPDATE Inventory SET EbayPrice='" + ebayprice + "' WHERE Sku = '" + sku + "';")
                print("Updated ebayprice of" + sku)
            if cat != "":
                self.mycursor.execute("UPDATE Inventory SET cat='" + cat + "' WHERE Sku = '" + sku + "';")

            self.mydb.commit()

    def addToInvenotory(self,sku,name,qty,quality,rare,selling,location,tcgplayerentry,ebaypriceentry,cat):
        print("INSERT INTO Inventory (sku,name,qty,quality,rare,selling,location,TCGPrice,EbayPrice,Cat) VALUES ('" + name + "','" + qty + "');")
        self.mycursor.execute("INSERT INTO Inventory (sku,name,qty,quality,rare,selling,location,TCGPrice,EbayPrice,Cat) VALUES ('" + sku + "','" + name + "','" + qty + "','" + quality + "','" + rare + "','" + selling + "','" + location + "','" + tcgplayerentry + "','" + ebaypriceentry + "','" + cat + "');")

        self.mydb.commit()

    def get_table(self,search,table):
        self.mycursor.execute("SELECT " + str(search) + " FROM " + str(table))

        return self.mycursor.fetchall()

    def searchOrders(self, searchterm,cat):
        if cat == None:
            print("SELECT * FROM Orders WHERE items LIKE " + "'%" +str(searchterm) + "%';")
            self.mycursor.execute("SELECT * FROM Orders WHERE items LIKE " + "'%" +str(searchterm) + "%';")
        else:
            print("SELECT * FROM Orders WHERE " + cat + " LIKE " + "%" +str(searchterm) + "%;")
            self.mycursor.execute("SELECT * FROM Orders WHERE " + cat + " LIKE " + "'%" +str(searchterm) + "%';")

        return self.mycursor.fetchall()
    
    def searchInventory(self, searchterm, cat):

        if cat == None:
            print("SELECT * FROM Inventory WHERE name LIKE " + "'%" +str(searchterm) + "%';")
            self.mycursor.execute("SELECT * FROM Inventory WHERE sku LIKE " + "'%" +str(searchterm) + "%';")
        else:
            #print(searchterm + " " + cat)
            print("SELECT * FROM Inventory WHERE " + cat + " LIKE " + "%" +str(searchterm) + "%;")
            self.mycursor.execute("SELECT * FROM Inventory WHERE " + cat + " LIKE " + "'%" +str(searchterm) + "%';")

        return self.mycursor.fetchall()

    

class shipstation():

    def create_order(self, ordernumber, orderdate, orderstatus, customeremail, billto, shipto, item, pay, text, shippingamount, tags):
        values = """
        {
            "orderNumber": " """ + ordernumber + """,
            "orderKey": "null",
            "orderDate": """ + orderdate +  """,
            "paymentDate": "null,
            "shipByDate": "null",
            "orderStatus": """ + orderstatus + """,
            "customerId": 37701499,
            "customerUsername": "null",
            "customerEmail": """ + customeremail + """",
            "billTo": {""" + billto + """
            },
            "shipTo": {""" + shipto + """
            },
            "items": """ + item + """
            "amountPaid": """ + pay + """,
            "taxAmount": null,
            "shippingAmount": null,
            "customerNotes": null,
            "internalNotes": null,
            "gift": false,
            "giftMessage": null,
            "paymentMethod": null,
            "requestedShippingService": null,
            "carrierCode": null,
            "serviceCode": null,
            "packageCode": null,
            "confirmation": null,
            "shipDate": null,
            "weight": null,
            "dimensions": {
            "units": null,
            "insuranceOptions": null,
            "internationalOptions": null,
            "advancedOptions": null,
            "tagIds": [
                """ + tag + """
            ]
        }
        """

        auth = base64.b64encode("4b42163a2344409780dca83c93aac587:a7bc884a9a60406da98ef7bb5de978c8".encode('utf-8'))
        
        headers = {
            'Authorization': 'Basic ' + auth.decode("utf-8")
        }

        print(values)

        #request = requests.get('https://ssapi.shipstation.com/orders?sortBy=OrderDate&sortDir=DESC', data=values ,headers=headers)

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

def Filldata(searchterm, table, cat):
    try:
        print("Filldata(" + searchterm + " " + table + " " + cat)
    except TypeError:
        print("Error in filldata")

    if table == "Orders":
        if searchterm != None:
            fetch = db.searchOrders(searchterm, Orderselectedcategory)

            for data in fetch:
                tree.insert("", 'end', values=(data))

        else:
            fetch = db.getOrders()

            for data in fetch:
                tree.insert("", 'end', values=(data))
    elif table == "Inventory":
        print("Test2")
        if searchterm != None:
            fetch = db.searchInventory(searchterm, Inventoryselectedcategori)

            for data in fetch:
                tree2.insert("", 'end', values=(data))

        else:
            fetch = db.getInventory()

            for data in fetch:
                tree2.insert("", 'end', values=(data))

def home():
    global root

    global Inventoryselectedcategori
    global Orderselectedcategory

    Orderselectedcategory = "name"
    Inventoryselectedcategori = "name"

    root = tk.Tk()
    root.title("SimplyInventory")
    width = 1500
    height = 1000
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenmmheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (width/2)

    root.geometry("1500x1000")
    #root.resizable(0,0)

    banner = tk.Frame(root)
    banner.pack(pady=10)

    #titleBanner = tk.Label(banner, text="Simply Inventory")
    #titleBanner.pack()
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu2 = tk.Menu(menubar, tearoff=0)
    menu3 = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=AddToInvenotory)
    filemenu2.add_command(label="View", command=ShowView)
    filemenu2.add_command(label="Edit", command=lambda: editscreen("Inventory"))
    filemenu2.add_command(label="Refresh", command=lambda: refresh("Inventory"))
    menu3.add_command(label="Refresh", command=lambda: refresh("Orders"))
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    menubar.add_cascade(label="Order", menu=menu3)  
    root.config(menu=menubar)
    root.config(bg="#99ff99")

    tabControl = ttk.Notebook(root)

    global Tab1 
    Tab1 = ttk.Frame(tabControl)
    global Tab2 
    Tab2 = ttk.Frame(tabControl)
    global Tab3 
    Tab3 = ttk.Frame(tabControl)
    global Tab4 
    Tab4 = ttk.Frame(tabControl)

    tabControl.add(Tab1, text="Orders")
    tabControl.add(Tab2, text="Inventory")
    tabControl.add(Tab3, text="Orders")
    tabControl.add(Tab4, text="Out of stock")
    tabControl.pack(expand = True, fill="both")

def ViewFormOrders():
    global tree
    TopViewForm = tk.Frame(Tab1, bd=1, relief=tk.SOLID)
    TopViewForm.pack(side=tk.TOP, fill=tk.X)
    LeftViewForm = tk.Frame(Tab1)
    LeftViewForm.pack(side=tk.LEFT, fill=tk.Y)
    MidViewForm = tk.Frame(Tab1)
    MidViewForm.pack(side=tk.LEFT, fill="both")
    #lbl_text = tk.Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    #lbl_text.pack(fill=tk.X)
    lbl_txtsearch = tk.Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=tk.TOP, anchor=tk.W)
    global search 
    search = tk.Entry(LeftViewForm, font=('arial', 15))
    search.pack(side=tk.TOP,  padx=10)
    btn_search = tk.Button(LeftViewForm, text="Search", command=lambda: Search("Orders"))
    btn_search.pack(side=tk.TOP, padx=10, pady=10)
    btn_delete = tk.Button(LeftViewForm, text="Delete")
    btn_delete.pack(side=tk.TOP, padx=10, pady=10)
    sortbybtn = tk.Button(LeftViewForm, text="SortBy", command=lambda: sort("Orders"))
    sortbybtn.pack(side=tk.TOP, padx=10, pady=10)
    scrollbarx = tk.Scrollbar(MidViewForm, orient=tk.HORIZONTAL)
    scrollbary = tk.Scrollbar(MidViewForm, orient=tk.VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("OrderDate", "Product Name", "Product Qty", "Product Price", "Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
    tree.heading('OrderDate', text="OrderDate",anchor=tk.W)
    tree.heading('Product Name', text="Order Date",anchor=tk.W)
    tree.heading('Product Qty', text="Order Address",anchor=tk.W)
    tree.heading('Product Price', text="Order Items",anchor=tk.W)
    tree.heading('Price', text="Order Price")
    tree.column('#0', stretch=tk.NO, minwidth=0, width=0)
    tree.column('#1', stretch=tk.NO, minwidth=0, width=200)
    tree.column('#2', stretch=tk.NO, minwidth=0, width=200)
    tree.column('#3', stretch=tk.NO, minwidth=0, width=320)
    tree.column('#4', stretch=tk.NO, minwidth=0, width=1020)
    tree.column('#5', stretch=tk.NO, minwidth=0, width=220)
    tree.pack()
    Filldata(None, "Orders", None)

def sort(table):
    global sortscreen

    sortscreen = tk.Tk()

    v = tk.IntVar()

    v.set(1)

    catsInventory = [
        ("sku", 1),
        ("name", 2),
        ("price", 3),
        ("cat", 4),
        ("rare", 5)
    ]

    catsOrders = [
        ("ordernumber", 1),
        ("name", 2),
        ("time", 3),
        ("address", 4),
        ("items", 5),
        ("price", 6),
        ("orgin", 7)
    ]

    if table == "Inventory":
        tk.Radiobutton(sortscreen, text=catsInventory[0][0], variable=v, value=1, command=lambda: setInventorycats(catsInventory[0][0], "Inventory")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsInventory[1][0], variable=v, value=2, command=lambda: setInventorycats(catsInventory[1][0], "Inventory")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsInventory[2][0], variable=v, value=3, command=lambda: setInventorycats(catsInventory[2][0], "Inventory")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsInventory[3][0], variable=v, value=4, command=lambda: setInventorycats(catsInventory[3][0], "Inventory")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsInventory[4][0], variable=v, value=5, command=lambda: setInventorycats(catsInventory[4][0], "Inventory")).pack(anchor=tk.W)
    if table == "Orders":
        tk.Radiobutton(sortscreen, text=catsOrders[0][0], variable=v, value=1, command=lambda: setInventorycats(catsOrders[0][0], "Orders")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsOrders[1][0], variable=v, value=2, command=lambda: setInventorycats(catsOrders[1][0], "Orders")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsOrders[2][0], variable=v, value=3, command=lambda: setInventorycats(catsOrders[2][0], "Orders")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsOrders[3][0], variable=v, value=4, command=lambda: setInventorycats(catsOrders[3][0], "Orders")).pack(anchor=tk.W)
        tk.Radiobutton(sortscreen, text=catsOrders[4][0], variable=v, value=5, command=lambda: setInventorycats(catsOrders[4][0], "Orders")).pack(anchor=tk.W)

    submitbtn = tk.Button(sortscreen, text="Set", command = sortscreen.destroy)
    submitbtn.pack(anchor=tk.W)

def setInventorycats(cat, table):
    if table == "Inventory":
        print("Set Inv Cat to " + cat)

        global Inventoryselectedcategori

        Inventoryselectedcategori = cat
    if table == "Orders":
        print("Set Odr cat to " + cat)

        global Orderselectedcategory

        Orderselectedcategory = cat

def ViewFormInventory():
    global tree2
    TopViewForm = tk.Frame(Tab2, bd=1, relief=tk.SOLID)
    TopViewForm.pack(side=tk.TOP, fill=tk.X)
    LeftViewForm = tk.Frame(Tab2)
    LeftViewForm.pack(side=tk.LEFT, fill=tk.Y)
    MidViewForm = tk.Frame(Tab2)
    MidViewForm.pack(side=tk.LEFT, fill="both")
    lbl_txtsearch = tk.Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=tk.TOP, anchor=tk.W)
    global searchInventory
    searchInventory = tk.Entry(LeftViewForm, font=('arial', 15))
    searchInventory.pack(side=tk.TOP,  padx=10)
    btn_search = tk.Button(LeftViewForm, text="Search", command=lambda: Search("Inventory"))
    btn_search.pack(side=tk.TOP, padx=10, pady=10)
    sortbybtn = tk.Button(LeftViewForm, text="SortBy", command=lambda: sort("Inventory"))
    sortbybtn.pack(side=tk.TOP, padx=10, pady=10)
    btn_delete = tk.Button(LeftViewForm, text="Delete")
    btn_delete.pack(side=tk.TOP, padx=10, pady=10)
    scrollbarx = tk.Scrollbar(MidViewForm, orient=tk.HORIZONTAL)
    scrollbary = tk.Scrollbar(MidViewForm, orient=tk.VERTICAL)
    tree2 = ttk.Treeview(MidViewForm, columns=("sku", "name", "qty", "quality", "rare", "selling", "loaction", "tcgprice", "Ebayprice", "cat" ), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree2.yview)
    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbarx.config(command=tree2.xview)
    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
    tree2.heading('sku', text="sku",anchor=tk.W)
    tree2.heading('name', text="name",anchor=tk.W)
    tree2.heading('qty', text="qty",anchor=tk.W)
    tree2.heading('quality', text="Qty",anchor=tk.W)
    tree2.heading('rare', text="rare",anchor=tk.W)
    tree2.heading('selling', text="selling",anchor=tk.W)
    tree2.heading('loaction', text="loaction",anchor=tk.W)
    tree2.heading('tcgprice', text="tcgprice",anchor=tk.W)
    tree2.heading('Ebayprice', text="Ebayprice",anchor=tk.W)
    tree2.heading('cat', text="cat",anchor=tk.W)
    tree2.column('#0', stretch=tk.NO, minwidth=0, width=0)
    tree2.column('#1', stretch=tk.NO, minwidth=0, width=200)
    tree2.column('#2', stretch=tk.NO, minwidth=0, width=200)
    tree2.column('#3', stretch=tk.NO, minwidth=0, width=30)
    tree2.column('#4', stretch=tk.NO, minwidth=0, width=30)
    tree2.column('#5', stretch=tk.NO, minwidth=0, width=80)
    tree2.column('#6', stretch=tk.NO, minwidth=0, width=80)
    tree2.column('#7', stretch=tk.NO, minwidth=0, width=80)
    tree2.column('#8', stretch=tk.NO, minwidth=0, width=80)
    tree2.column('#9', stretch=tk.NO, minwidth=0, width=80)
    tree2.column('#10', stretch=tk.NO, minwidth=0, width=80)
    tree2.pack()
    Filldata(None, "Inventory", None)

def refresh(table):
    
    if table == "Orders":
        tree.delete(*tree2.get_children())
    elif table == "Inventory":
        tree2.delete(*tree2.get_children())

    Filldata(None, table, None)

def edit(tabel,sku,name,qty,quality,rare,selling,location,tcgplayer,ebayprice,cat):

    #itemsku = getSelectedItem("Inventory")

    #print(itemsku[1])

    db.updateRow(sku, name.get(),qty.get(),quality.get(),rare.get(),selling.get(),location.get(),tcgplayer.get(),ebayprice.get(),cat.get())

    editscreen.destroy()

def Logout():
    print("LOGOUT")

def Exit2():
    quit()

def ShowAddNew():
    print("SHOWADDNEW")

def ShowView():
    print("SHOWVIEW")

def getSelectedItem(tabel):
    if tabel == "Orders":
        curitems = tree.focus()
        return tree.selection()[0]
    if tabel == "Inventory":
        item = tree2.selection()

        inventory = db.getInventory()

        for i in range(len(item)):
            itemnums = re.sub("\D", "", item[i])

            return db.getRowFromInventory(int(itemnums))


def editscreen(tabel):
    global editscreen

    editscreen = tk.Tk()

    editscreen.title("Edit")

    editscreen.geometry("200x230")

    item = getSelectedItem("Inventory")

    tk.Label(editscreen, text="Sku").grid(row=0, column=0)
    skuentry = tk.Entry(editscreen, text=item)
    tk.Label(editscreen, text="Name").grid(row=1, column=0)
    nameentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="qty").grid(row=2, column=0)
    qtyentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="quality").grid(row=3, column=0)
    qualityentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="rare").grid(row=4, column=0)
    rareentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="selling").grid(row=5, column=0)
    sellingentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="location").grid(row=6, column=0)
    locationentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="tcgplayer").grid(row=7, column=0)
    tcgplayerentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="Ebayprice").grid(row=8, column=0)
    ebaypriceentry = tk.Entry(editscreen)
    tk.Label(editscreen, text="cat").grid(row=9, column=0)
    catentry = tk.Entry(editscreen)

    skuentry.grid(row=0, column=1)
    nameentry.grid(row=1, column=1)
    qtyentry.grid(row=2, column=1)
    qualityentry.grid(row=3, column=1)
    rareentry.grid(row=4, column=1)
    sellingentry.grid(row=5, column=1)
    locationentry.grid(row=6, column=1)
    tcgplayerentry.grid(row=7, column=1)
    ebaypriceentry.grid(row=8, column=1)
    catentry.grid(row=9, column=1)

    submitbutton = tk.Button(editscreen, text="Submit", command=lambda: edit(tabel,skuentry,nameentry,qtyentry,qualityentry,rareentry,sellingentry,locationentry,tcgplayerentry,ebaypriceentry,catentry))

    submitbutton.grid(row=10, column=0)

def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter != None:
            print("You selected", model[treeiter][0])

def Search(Tabel):
    if Tabel == "Orders":
        if search.get() != "":
            print("Search(" + Tabel + ") + " + Orderselectedcategory)
            tree.delete(*tree.get_children())
            Filldata(search.get(), "Orders",Orderselectedcategory)
        else:
            tree.delete(*tree.get_children())
            Filldata(None, "Orders",Orderselectedcategory)
    elif Tabel == "Inventory":
        if searchInventory.get() != "":
            #print(searchInventory.get() + " " + selectedcategori)
            tree2.delete(*tree2.get_children())
            Filldata(searchInventory.get(), "Inventory",Inventoryselectedcategori)
        else:
            tree2.delete(*tree2.get_children())
            Filldata(None, "Inventory",Inventoryselectedcategori)

def AddToInvenotory():
    
    global addscreen

    addscreen = tk.Tk()

    addscreen.title("Add")

    addscreen.geometry("200x230")

    tk.Label(addscreen, text="Sku").grid(row=0, column=0)
    skuentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="Name").grid(row=1, column=0)
    nameentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="qty").grid(row=2, column=0)
    qtyentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="quality").grid(row=3, column=0)
    qualityentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="rare").grid(row=4, column=0)
    rareentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="selling").grid(row=5, column=0)
    sellingentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="location").grid(row=6, column=0)
    locationentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="tcgplayer").grid(row=7, column=0)
    tcgplayerentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="Ebayprice").grid(row=8, column=0)
    ebaypriceentry = tk.Entry(addscreen)
    tk.Label(addscreen, text="cat").grid(row=9, column=0)
    catentry = tk.Entry(addscreen)

    print("Adding the Entry's")

    skuentry.grid(row=0, column=1)
    nameentry.grid(row=1, column=1)
    qtyentry.grid(row=2, column=1)
    qualityentry.grid(row=3, column=1)
    rareentry.grid(row=4, column=1)
    sellingentry.grid(row=5, column=1)
    locationentry.grid(row=6, column=1)
    tcgplayerentry.grid(row=7, column=1)
    ebaypriceentry.grid(row=8, column=1)
    catentry.grid(row=9, column=1)

    submitbutton = tk.Button(addscreen, text="Submit", command=lambda: submitToInventory(skuentry,nameentry,qtyentry,qualityentry,rareentry,sellingentry,locationentry,tcgplayerentry,ebaypriceentry,catentry))

    submitbutton.grid(row=10, column=0)

def submitToInventory(sku,name,qty,quality,rare,selling,location,tcgplayerentry,ebaypriceentry,cat):
    db.addToInvenotory(sku.get(),name.get(),qty.get(),quality.get(),rare.get(),selling.get(),location.get(),tcgplayerentry.get(),ebaypriceentry.get(),cat.get())
    addscreen.destroy()

def Login():

    def check_creds(root, username, password):

        if username == "SimplyUnlucky" and password == "ez":
            root.destroy()
        else:
            Login()

    screen_frame = tk.Tk()

    screen_frame.geometry("300x100")

    username = tk.Entry(screen_frame, text="Username")
    password = tk.Entry(screen_frame, text="Password")
    login_button = tk.Button(screen_frame, text='Login', command=lambda: check_creds(screen_frame, username.get(), password.get()))

    username.pack()
    password.pack()
    login_button.pack()

    screen_frame.mainloop()


def main():
    sp.create_order("SBAD-EN002", "11/15/2019", "awaiting_shippment", "MPearsonpear@protonmail.com", )
    Login()
    home()
    ViewFormOrders()
    ViewFormInventory()
    root.mainloop()


db = mysqlDatabase()
sp = shipstation()
main()