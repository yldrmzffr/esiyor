
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
    print("*******************\n")
    sehir_sec("sehir")

