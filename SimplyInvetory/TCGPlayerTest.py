import request

url = "http://api.tcgplayer.com/v1.32.0/stores/storeKey/orders/orderNumber/items"

response = requests.request("GET", url)