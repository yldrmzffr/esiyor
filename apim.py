import json
import requests
class havalar():

    sehir = None

    def __init__(self):
        pass
    def get_info(self,sehir):
        self.sehir = sehir
        try:
            data = requests.get("http://api.openweathermap.org/data/2.5/weather?q={id}&appid=fe76c224322cdde0049342cb45d26b04".format(id=sehir)).content.decode('utf-8')
            return data
         except:
            print("Error: Can not reach ")

hava = havalar()
hava.get_info("KONYA")
