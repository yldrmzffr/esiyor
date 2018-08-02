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
        print("\n\n\n                   	 {}          ".format(sehir))
        my_wheather_list = [weather_main, description, temp, humidity, temp_min, temp_max, speed]
        #print(my_wheather_list)
        veri=my_wheather_list
        desc = veri[1].find("broken")
        name = veri[0]
        temp = veri[2]
        maxt = veri[5]
        mint = veri[4]
        nem = veri[3]
        hiz = veri[6]

        clear = ("""
                      \   /     {name}
                       .-.      {temp}
                    ― (   ) ―   {max}-{min}
                       `-’      {nem}
                      /   \     -->{hiz}
                 """).format(name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)
        parcali = ("""

                     \  /       {name}
                   _ /"".-.     {temp}
                     \_(   ).   {max}-{min}
                     /(___(__)  {nem}



                 """).format(name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

        hard = ("""

                       .-.      {name}
                      (   ).    {temp}
                     (___(__)   {max}-{min}
                    ‚‘⚡‘‚⚡‚‘    {nem}
                                 {hiz}
                 """).format(name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

        yagmur = ("""


                   _`/"".-.     {name}
                    ,\_(   ).   {temp}
                     /(___(__)  {max}-{min}
                     ‚‘‚‘‚‘‚‘   {nem}
                                 {hiz}
                 """).format(name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

        kar = ("""

                      .-.       {name}
                     (   ).     {temp}
                    (___(__)    {max}-{min}
                     * * * *    {nem}
                     * * * *    {hiz}

                 """).format(name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

        sis = ("""

                 _ - _ - _ -    {name}
                 _ - _ - _      {temp}
                 _ - _ - _ -    {max}-{min}
                                {nem}
                                {hiz}

                 """).format(name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

        yok=("""

                      |===\      {name}
                      |    |     Temp{temp}
                      | * *|     {max}-{min}
                      |  | |     {nem}
                      |-//-|     {hiz}
                      ------

                     """).format(name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)
        temp = veri[2]
        maxt = veri[5]
        mint = veri[4]
        nem = veri[3]
        hiz = veri[6]
        if veri[0] == "Clear":
            print(clear)
        elif veri[0] == "Rain" :
            print(yagmur)
        elif veri[0] == "Fog":
            print(sis)
        elif veri[0] == "Clouds":
            print(parcali)
        else:
            print(yok)
