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
        sehir=sehir.upper()
        return sehir

    else:
        print("Incorrect Enter: Try again. \n")
        menu()

print("*******************\n")
print("    WELCOME      \n")
print("\n")
print("*******************\n")


while True:


    sehir=menu()
    sehir=buyut(sehir)

    weather_main=hava.get_info(sehir).get("weather")[0].get("main")
    print(weather_main)
    description = hava.get_info(sehir).get("weather")[0].get("description")
    print(description)
    temp = hava.get_info(sehir).get("main").get("temp")
    print(temp)
    humidity=hava.get_info(sehir).get("main").get("humidity")
    print(humidity)