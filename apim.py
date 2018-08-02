import Esemeyen_sinifi
hava = Esemeyen_sinifi.Havalar()


def buyut(sehir):
	sehirbuyuk=sehir.upper()
	translationTable = str.maketrans("ĞÜŞÖÇİ", "GUSOCI")
	sehirbuyuk = sehirbuyuk.translate(translationTable)

	return sehirbuyuk



def menu():
    konum=hava.auto_get()
    print("suan {} şehrindesiniz".format(konum))
    print("yapmak istediğiniz işlemi seçiniz : ")
    print("0 : Bulunduğunuz şehrin hava durumu")
    print("1 : Baska bir şehir")
    secim = input("seciminizi yapınız : ")


    if secim == "0":
       ## Konuma gore cagir.
       return konum


    elif secim == "1":
        sehir=input("şehir ismi giriniz : ")
        sehir=sehir.upper()
        return sehir

    else:
        print("Yanlış seçim yaptınız.Lütfen tekrar seçim yapınız \n")
        menu()

print("*******************\n")
print("    HOSGELDİNİZ      \n")
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