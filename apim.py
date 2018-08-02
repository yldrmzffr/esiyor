import Esemeyen_sinifi
hava = Esemeyen_sinifi.Havalar()


def buyut(sehir):
	sehirbuyuk=sehir.upper()
	translationTable = str.maketrans("ĞÜŞÖÇİ", "GUSOCI")
	sehirbuyuk = sehirbuyuk.translate(translationTable)

	return sehirbuyuk



def menu():
    konum=hava.auto_get()
    print("Current Location:{}".format(konum))
    print("Menu: ")
    print("0 : Current Location")
    print("1 : Another Location")
    secim = input("Please Enter Choice ")



    if secim == "0":
       ## Konuma gore cagir.
       return konum


    elif secim == "1":
        sehir=input("Please Enter New City : ")

        return sehir

    else:
        print("Incorrect Enter: Try again. \n")
        menu()

print("*******************\n")
print("      WELCOME    \n ")
print("*******************\n")


while True:


    sehir=menu()
    sehir=buyut(sehir)
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

        my_wheather_list = [weather_main, description, temp, humidity, temp_min, temp_max, speed]
        print(my_wheather_list)
