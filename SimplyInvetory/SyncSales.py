from openpyxl import load_workbook
import base64
import requests
import mysql.connector

sku_column = 0
name_column = 1
qty_column = 2
quality_column = 3
rare_column = 4
selling_column = 5
location_column = 6
ebayprice_column = 7
tcgplayer_column = 8

def syncsales():
    
    current_inventory = db.getInventory()

    for i in range(len(current_inventory)):
        if current_inventory[i][selling_column] == "y":
            db.addToSales(current_inventory[i][sku_column],current_inventory[i][name_column],current_inventory[i][qty_column],current_inventory[i][location_column],current_inventory[i][9],current_inventory[i][8])
        elif current_inventory[i][selling_column] == "n":
            db.removeFromSales(current_inventory[i][sku_column])

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

    def resetOrders(self):

        self.mycursor.execute

    def removeFromSales(self, sku):

        self.mycursor.execute("DELETE FROM Sales WHERE sku=" + "'" + str(sku) + "';")
        self.mydb.commit()

    def addToSales(self, sku, name, qty, location, ebayprice, tcgprice):

        try:
            sku = sku.replace("'", " ")
        except:
            pass
        try:
            name = name.replace("'", " ")
        except:
            pass
        try:
            qty = qty.replace("'", " ")
        except:
            pass
        try:
            location = location.replace("'", " ")
        except:
            pass
        try:
            ebayprice = ebayprice.replace("'", " ")
        except:
            pass
        try:
            tcgprice = tcgprice.replace("'", " ")
        except:
            pass

        try:
            print("INSERT INTO Sales (sku, name, qty, location) VALUES ('" + str(sku) + "','" + str(name) + "','" + str(qty) + "','" + str(location) + "');")
            self.mycursor.execute("INSERT INTO Sales (sku, name, qty, location) VALUES ('" + str(sku) + "','" + str(name) + "','" + str(qty) + "','" + str(location) + "','" + str(ebayprice) + "','" + str(tcgprice) + "');")
            self.mydb.commit()
        except:
            print("Updates " + sku)
            self.mycursor.execute("DELETE FROM Sales WHERE sku=" + "'" + str(sku) + "';")
            self.mycursor.execute("INSERT INTO Sales (sku, name, qty, location) VALUES ('" + str(sku) + "','" + str(name) + "','" + str(qty) + "','" + str(location) + "');")
            self.mydb.commit()
        

    def addToOrders(self, ordernumber, time, address, items, qty, price, orgin):
        #print("INSERT INTO Orders (ordernumber, time, address, items, price, orgin) VALUES ('" + ordernumber + "','" + time + "','" + address + "','" + items + "','" + price + "','" + orgin + "');")

        #command = "INSERT INTO Orders (ordernumber, time, address, items, price, orgin) VALUES (%s, %s, %s, %s, %s, %s)"
        #vals = (ordernumber, time, address, items, price, orgin)

        #self.mycursor.execute(command, vals)

        final_items = ""

        for i in range(len(items)):
            final_items = final_items + items[i] + " Qty: " + str(qty[i])

        try:
            final_items = final_items.replace("'", " ")
        except:
            pass
        try:
            ordernumber = ordernumber.remove("'")
        except:
            pass
        try:
           time = time.remove("'")
        except:
            pass
        try:
            price = price.remove("'")
        except:
            pass
        try:
            orgin = orgin.remove("'")
        except:
            pass
        try:
            address = address.remove("'")
        except:
            pass
        
        try:
            try:
                print("INSERT INTO Orders (ordernumber, time, address, items, price, orgin) VALUES ('" + str(ordernumber) + "','" + str(time) + "','" + str(address) + "','" + str(final_items) + "','" + str(price) + "','" + str(orgin) + "');")
                self.mycursor.execute("INSERT INTO Orders (ordernumber, time, address, items, price, orgin) VALUES ('" + str(ordernumber) + "','" + str(time) + "','" + str(address) + "','" + str(final_items) + "','" + str(price) + "','" + str(orgin) + "');")
                self.mydb.commit()
            except mysql.connector.errors.IntegrityError:
                print("WHY ERROR")
                self.mycursor.execute("DELETE FROM Orders;")
                self.mydb.commit()
        except mysql.connector.errors.ProgrammingError:
            print("FUCK UP CARD ")
            pass

db = mysqlDatabase()
syncsales()