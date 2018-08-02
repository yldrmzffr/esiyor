import json
import requests
class Havalar():
    sehir = None
    def init(self):
        pass
    def get_info(self,sehir):
        self.sehir = sehir
        try:
            data = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q={id}&appid=fe76c224322cdde0049342cb45d26b04".format(id=sehir)).content.decode('utf-8'))
            return data
        except:
            print("Error: Can not reach ")


    def auto_get(self):
        data = json.loads(requests.get("https://ipapi.co/json").content.decode('utf-8')).get("city")
        if data == None:
            data = json.loads(requests.get("http://ip-api.com/json").content.decode('utf-8')).get("city")
            if data == None:
                data = json.loads(requests.get("http://extreme-ip-lookup.com/json/").content.decode('utf-8')).get("city")

        self.sehir = data
        return data
