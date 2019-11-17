from openpyxl import load_workbook
import base64
import requests
import mysql.connector

#workbook = load_workbook(filename="Order.xlsx")
#sheet = workbook.active

#sheet["A3"] = "SOFU-EN041"
#sheet["B3"] = "Dinowrestler King T Wrextle"
#sheet["C3"] = 2
#sheet["D3"] = 4

def draw_forms_for_orders_from_shipstation():

            test = sp.get_orders() 

            for i in range(len(test["orders"])):

                items = []
                qty = []
                price = 0.0
                ordernumber = 0
                try:
                    print("-"*50)

                    ordernumber = test["orders"][i]["orderId"]

                    print(ordernumber)
                    #print(name_texting)

                    orderdate = test["orders"][i]["orderDate"]

                    print(orderdate)
                    #print(date_text)

                    address = test["orders"][i]["shipTo"]["city"] + " " + test["orders"][i]["shipTo"]["street1"]
                    #print(billto_text)
                    
                    test_item = test["orders"][i]["items"][0]["name"]
                    test_qty = test["orders"][i]["items"][0]["quantity"]

                    for x in range(len(test["orders"][i]["items"])):
                        print(items)
                        print(qty)
                        #print(len(test["orders"][i]["items"]))
                        items.append(test["orders"][i]["items"][x]["name"])
                        qty.append(test["orders"][i]["items"][x]["quantity"])

                    price = test["orders"][i]["orderTotal"]

                    db.addToOrders(ordernumber, orderdate, address, items, qty, price, "Shipstation")

                except NameError:
                    continue

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

        self.mycursor.execute("SELECT * FROM Orders")

        myresult = self.mycursor.fetchall()

        return myresult

    def resetOrders(self):

        self.mycursor.execute

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
                return
        except mysql.connector.errors.ProgrammingError:
            print("FUCK UP CARD ")
            pass

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

db = mysqlDatabase()
sp = shipstation()

draw_forms_for_orders_from_shipstation()

#workbook.save(filename="Inventory.xlsx")