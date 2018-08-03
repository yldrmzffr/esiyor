import logging
import json
import requests

FORMAT='[%(asctime)s] [%(levelname)s] [%(message)s]'
logging.basicConfig(filename="logs.log", format=FORMAT, level=logging.INFO)


class Havalar():
    sehir = None
    def init(self):
        pass
    def get_info(self,sehir):
        self.sehir = sehir

        try:
            data = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q={id}&appid=fe76c224322cdde0049342cb45d26b04".format(id=sehir)).content.decode('utf-8'))
            if data.get("cod")==200:
                return data
            else:
                print("Invalid city name!!")
                logging.warning("Api Olumlu cevap vermedi. Cevap: {}".format(data))
                return None
        except:
            logging.Error("Hava Durumu API hiç çalışmadı..")
            print("Error: Can not reach ")


    def auto_get(self):
        try:
            logging.info("1. API (ipapi) deneniyor..")
            data = json.loads(requests.get("https://ipapi.co/json").content.decode('utf-8')).get("city")
            logging.info("Gelen Veri: {}".format(data))
            if data == None:
                logging.warning("1. API (ipapi) Data vermedi..")
                logging.info("2. API (ip-api) deneniyor..")
                data = json.loads(requests.get("http://ip-api.com/json").content.decode('utf-8')).get("city")
                logging.info("Gelen Veri: {}".format(data))
                if data == None:
                    logging.warning("2. API (ip-api) Data vermedi..")
                    logging.info("3. API (extreme-ip-lookup) deneniyor..")
                    data = json.loads(requests.get("http://extreme-ip-lookup.com/json/").content.decode('utf-8')).get("city")
                    logging.info("Gelen Veri: {}".format(data))
            self.sehir = data
            return data
        except:
            logging.Error("Konum API hiç çalışmadı.")
            print("İnternet Bağlatınızı Kontrol Edin.")
            logging.info("Uygulama Kapatılıyor")
            exit()
