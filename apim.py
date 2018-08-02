import Esemeyen_sinifi
hava = Esemeyen_sinifi.Havalar()

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

while True:
    print("*******************\n")
    print("    HOSGELDİNİZ      \n")
    print("\n")
    print("*******************\n")
    sehir=menu()

