import requests
import base64
import json
import os
import requests
from lxml import html

tcgplayerpublic = "47247B44-59EC-4CE5-ACC2-95E96F1447DF"
tcgplayerprivate = "C975F217-C201-40DD-B70A-7F45D511E3AA"
apllicationid = "5409"
storekey = "984035ec"

class tcgplayer():

    bearer = " "

    def getbearertoken(self):

        auth = "grant_type=client_credentials&client_id=" + tcgplayerpublic + "&client_secret=" + tcgplayerprivate

        header = {
            'Authorization': 'application/x-www-form-urlencoded',
        }

        r = requests.post(headers = header, url="https://api.tcgplayer.com/token", data = auth)

        data = r.json()

        self.bearer = data["access_token"]

    def getcatalog(self):

        header = {
            "Authorization": "bearer " + self.bearer
        }

        r = requests.get(headers = header, url="http://api.tcgplayer.com/v1.32.0/catalog/categories")

        data = r.json()

        print(data)

    def getordermanifest(self):
        header = {
            "Authorization": "bearer " + self.bearer
        }

        r = requests.get(headers = header, url="http://api.tcgplayer.com/v1.32.0/app/authorize/")

        data = r.json()

        print(data)

    def getorderaddress(self):

        payload = {
            'UserName': 'MPearsonpear@protonmail.com',
            'Password': '459799OoMatt!'
        }

        session_requests = requests.session()

        post = session_requests.post("https://store.tcgplayer.com/admin/account/logon", data=payload)
        r = session_requests.get("https://store.tcgplayer.com/admin/Seller/Dashboard/984035ec")
        finaltext = r #or whatever else you want to do with the request data!

        finaltext = finaltext.split("<div data-v-f4f66888 class='widget'>")

        finaltext2 = finaltext[1].split("<!--->")

        finaltext2 = finaltext2[1].split("<td>")

        finaltext2 = finaltext2[1].split("</td>")

        selection1 = finaltext2[1].split(">")

        selection1 = finaltext2[1].split("</a>")

        selection2 = finaltext2[2].split(">")

        selection2 = finaltext2[2].split("</a>")

        selection3 = finaltext2[3].split(">")

        selection3 = finaltext2[3].split("</a>")

        selection4 = finaltext2[5].split(">")

        selection4 = finaltext2[5].split("</a>")

        selection5 = finaltext2[6].split(">")

        selection5 = finaltext2[6].split("</a>")

        selection6 = finaltext2[7].split(">")

        selection6 = finaltext2[7].split("</a>")

        print(finaltext2[1])

        # r = requests.get("https://store.tcgplayer.com/admin/orders/manageorder/74645-D517A4-B6E30")

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

    def submit_order(self, orderNumber, orderDate, orderStatus, billTo, shipTo, items):
        auth = base64.b64encode("4b42163a2344409780dca83c93aac587:a7bc884a9a60406da98ef7bb5de978c8".encode('utf-8'))
        
        headers = {
            'Authorization': 'Basic ' + auth.decode("utf-8")
        }
        print(auth.decode("utf-8"))

        data = {
            'ordernumber': orderNumber,
            'orderdate': orderDate,
            'orderstatus': orderStatus,
            'billTo': billTo,
            'shipTo': shipTo
        }

        request = requests.get('https://ssapi.shipstation.com/orders/createorder', headers=headers, data = data)

        if request.status_code == "401":
            print("AWWWW FUCK")
            return

        responce = request.json()

        return responce

tcg = tcgplayer()
sp = shipstation()

tcg.getbearertoken()
tcg.getordermanifest()

order = {
    "name": "Matthew Pearson",
    "company": "",
    "street1": "2208 Lantern Drive",
    "city": "Modesto",
    "state": "California",
    "postalCode": "95355",
    "country": "US",
    "phone": "209-613-0489",
    "residential": "true",
}

Orderitem = {
    "sku": "SAST-EN02",
    "name": "Squirt squid",
    "shippingAmount": "3",
}


sp.submit_order("11111", "2019/11/26","cancelled", order, order, Orderitem)

