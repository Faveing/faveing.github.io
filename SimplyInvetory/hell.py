import requests

url = "http://api.tcgplayer.com/v1.32.0/stores/fe61bbf2/status/active"

response = requests.request("PUT", url)

print(response.text)
