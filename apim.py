import json
import requests
class havalar():
    sehir = None
    def init(self):
        pass
    def get_info(self,sehir):
        self.sehir = sehir
        try:
            data = requests.get("http://api.openweathermap.org/data/2.5/weather?q={id}&appid=fe76c224322cdde0049342cb45d26b04".format(id=sehir)).content.decode('utf-8')
            return data
        except:
            print("Error: Can not reach ")


    def auto_get(self):
        data = json.loads(requests.get("https://ipapi.co/json").content.decode('utf-8')).get("city")
        self.sehir = data
        return data

hava = havalar()

def sehir_sec(sehir):
    print("suan {} şehrindesiniz".format(sehir))
    print("yapmak istediğiniz işlemi seçiniz : ")
    print("0 : Bulunduğunuz şehrin hava durumu")
    print("1 : Baska bir şehir")
    secim = input("seciminizi yapınız : ")

    if secim.isnumeric():
        secim = int(secim)
    else:
        sehir_sec(sehir)

    if secim == 0:
       return sehir

    elif secim == 1:
        sehir=input("şehir ismi giriniz : ")
        sehir=sehir.upper()
        return sehir

    else:
        print("Yanlış seçim yaptınız.Lütfen tekrar seçim yapınız : \n")
        sehir_sec(sehir)

while True:
    print("*******************\n")
    print("    HOSGELDİNİZ      \n")
    print("\n")
    print("*******************\n")
    sehir_sec(hava.auto_get())
