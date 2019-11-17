import base64
import requests
import json

appid = "SimplyUn-SimplyIn-SBX-5b31f104d-afc503d2"
certid = "SBX-b31f104d81e2-3c80-4eae-b2e8-7c52"
devid = "c7bf7436-c92f-4bdb-b4ad-52ce562bc0f5"
app_token = "v^1.1#i^1#p^1#I^3#r^0#f^0#t^H4sIAAAAAAAAAOVYa2wUVRTuttuShkcVEMEQ2QxoIpuZvTP76gzs4m4fsFBodZemNEozO3OnHZiXc+/YXTSh1thEfmkIPpDUauKTQDS8fIHBRzQGI0HjA/mh0RiJjwiEYCSid2dLaSuBQlds4v65c+8959xzvnPOPWcv6KmqXti3rO/MVM+k8oEe0FPu8bCTQXVVpX9aRflNlWVgGIFnoGdBj7e34sfFSNQ1S7gTIss0EPTldM1AgrsYoxzbEEwRqUgwRB0iAUtCOrGySeAYIFi2iU3J1Chfqj5GZYMAiEEFhiCMKlyQJavGeZkZM0ZJHB+KRsISB+QQZKUo2UfIgSkDYdHAMYoDLE+zLA3CGS4ocKzAAgawkXbK1wptpJoGIWEAFXfVFVxee5iul1ZVRAjamAih4qlEY7o5kapvWJVZHBgmKz6IQxqL2EEjZ3WmDH2toubASx+DXGoh7UgSRIgKxIsnjBQqJM4rcxXqu1BHIxJbK0bCPBdVImGRLwmUjaati/jSehRWVJlWXFIBGljF+cshStDIroMSHpytIiJS9b7CcIcjaqqiQjtGNSQTaxItLVQ8reqWll9t0MWPFPlIttHhbJBVWBCSaVGRwiAoc4MHFaUNwjzqpDrTkNUCaMi3ysRJSLSGo7Fhh2FDiJqNZjuh4IJGQ3SRDGCHMOTaC04tetHBXUbBr1AnQPjc6eU9MMSNsa1mHQyHJIzecCGKUaJlqTI1etONxcHwyaEY1YWxJQQC3d3dTHeQMe3OAAcAG2hb2ZSWuqAuUoS2kOtFevXyDLTqmiJBwolUAectokuOxCpRwOik4sFgOMTzg7iPVCs+evUfC8NsDozMiFJliAJqo6IEasPhqJKtzYZKkSHxwSANFPSAWTFP66K9HmJLEyVISyTOHB3aqiwEw+T+q1UgLUd4hQ7xikJnw3KEZhUIAYTZrMTX/p8SZayhnoaSDXFJYr1kcZ7Mden+HFqTixhasq2zvd6QmhT/PWBde0OojrOWprDTzgGc78qg2Fiz4eLGS6YFW0xNlfIlQKCQ6yVEIWjLLaKN80knT+ZpqGlkGJe5qGDuxHJ1gR8RAaKlMoX0ZiRTD5giudcLSx2uxr6xEAWyTp7pdCDCRAuZlNYxM6kkPxhyS8hjZyneQcSAsbOQvk12JHxVB7mXHUOQVDu7MLqiM3MjQBlX9CQsK6XrDhazGkyVpjr+R5XxouappHccu02FXL8GdhHPFl2sysXGj3H9zKB7JcaGyHRs0vMyzYU+KGOuhwapKtg2NQ3arey4nT3BfHyFxffq7C5d5zeRYlvSVBI+HRPNsmviUVUcb3fj7fU8XmLL2XCU4/kIiIJx2Vbn+jWTn2hVfZmJMJT/hT8qgZHPJvEy98f2evaDXs/r5R4PQZRm/eC2qorV3oopFCLFnUGiIWfNHKOKCkNKqCFix4bMepi3RNUur/KoRz+Tfh/2YDNwN5g99GRTXcFOHvZ+A+Ze2Klka26cyvIsC8JckCNDO5h/YdfLzvLO5ObSC37t331QjQb+uLXq8Mml27a+B6YOEXk8lWUkusp6z664+WTiyKaP9zWeC2z5YZvqt6f5W7oHuKO5u2ZXTnv469d++zDw4PubP79+Y+rwgHJEX6DszV53n7716bnB5bv7Vkxf4uVC+x97cvGSY7/c/saUA3v6fae/2vC8/tbGtLxlh7L90RM7523yn271HVq0JnaIbplTPn1Xk9395YzwjP7DO5ufevbdt1/ZM6nmof7vqm/pcGYebJws8B9Zmec2vzQjeeon8dvj2w+kAhWfHudfnPPOMVV9Ien3bpj0/d5zp5d/8MWitQ8803XwrDVLa3iktf/P4FqjYvoh6sybibXmDfqOsPflb3hpfh93aiE1635nXt0TU5bu+mRfruavDt/MJa96f26bXXNiVtGNfwPmk7XeShMAAA=="

class Ebayapi():

    def getOffer(self):

        print("Running")

        headers = {
            'Authorization': 'Bearer ' + app_token
        }

        request = requests.get('https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?q=CRMS-EN031', headers=headers)

        print("RAN")

        print(request.json())

ebayapi = Ebayapi()

ebayapi.getOffer()