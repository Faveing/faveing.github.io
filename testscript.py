import requests
from lxml import html

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