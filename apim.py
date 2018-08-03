import logging
import EsemeyenSinif
import cizdir
hava = EsemeyenSinif.Havalar()


FORMAT='[%(asctime)s] [%(levelname)s] [%(message)s]'
logging.basicConfig(filename="logs.log", format=FORMAT, level=logging.INFO)


def buyut(sehir):
	sehirbuyuk=sehir.upper()
	translationTable = str.maketrans("ĞÜŞÖÇİ", "GUSOCI")
	sehirbuyuk = sehirbuyuk.translate(translationTable)
	logging.info("{} araması {} ile düzeltildi".format(sehir,sehirbuyuk))
	return sehirbuyuk



def menu():
    konum=hava.auto_get()
    logging.info("Konumu Tespit Edildi. Konumu: {}".format(konum))
    print("Current Location:{}".format(konum))
    print("Menu: ")
    print("0 : Current Location")
    print("1 : Another Location")
    secim = input("Please Enter Choice ")

    logging.info("Menuden {} seçildi.".format(secim))
    if secim == "0":
        return konum


    elif secim == "1":
        sehir=input("Please Enter New City : ")
        logging.info("{} Şehri için özel arama yapıldı.".format(sehir))
        return sehir

    else:
        print("Incorrect Enter: Try again. \n")
        logging.warning("{} destekleyan karakter..".format(secim))
        menu()

print("*******************\n")
print("      WELCOME    \n ")
print("*******************\n")
logging.info("HOŞGELDİN EKRANI BASILDI")


while True:
    sehir=buyut(menu())
    logging.info("{} ile sorgulama yapılmak istendi.".format(sehir))

    if  hava.get_info(sehir)==None:
        menu()
    else:
        weather_main=hava.get_info(sehir).get("weather")[0].get("main")
        description = hava.get_info(sehir).get("weather")[0].get("description")
        temp = hava.get_info(sehir).get("main").get("temp")
        temp=int(temp)-272
        humidity=hava.get_info(sehir).get("main").get("humidity")
        temp_min = hava.get_info(sehir).get("main").get("temp_min")
        temp_min=int(temp_min)-272
        temp_max = hava.get_info(sehir).get("main").get("temp_max")
        temp_max=int(temp_max)-272
        speed = hava.get_info(sehir).get("wind").get("speed")
        print("\n\n\n                   	 {}          ".format(sehir))
        my_wheather_list = [weather_main, description, temp, humidity, temp_min, temp_max, speed]
        cizdir.load(my_wheather_list)
        logging.info("Hava durumu goruntelendi")
