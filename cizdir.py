def load(veri):
    desc = veri[1]
    name = veri[0]
    temp = veri[2]
    maxt = veri[5]
    mint = veri[4]
    nem = veri[3]
    hiz = veri[6]
    clear = ("""
                  \   /     {name}({desc})
                   .-.      Temp: {temp}
                ― (   ) ―   Max-Min Temp: {max} - {min}
                   `-’      Hum: {nem}
                  /   \     WndSpd: {hiz}
             """).format(desc=desc,name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)
    parcali = ("""

                 \  /       {name}({desc})
               _ /"".-.     Temp: {temp}
                 \_(   ).   Max-Min Temp: {max} - {min}
                 /(___(__)  Hum: {nem}
                            WndSpd: {hiz}

             """).format(desc=desc,name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

    hard = ("""

                   .-.      {name}({desc})
                  (   ).    Temp: {temp}
                 (___(__)   Max-Min Temp: {max} - {min}
                ‚‘⚡‘‚⚡‚‘    Hum: {nem}
                            WndSpd: {hiz}
             """).format(desc=desc,name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

    yagmur = ("""


               _`/"".-.     {name}({desc})
                ,\_(   ).   Temp: {temp}
                 /(___(__)  Max-Min Temp: {max} - {min}
                 ‚‘‚‘‚‘‚‘   Hum: {nem}
                            WndSpd: {hiz}
             """).format(desc=desc,name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

    kar = ("""

                  .-.       {name}({desc})
                 (   ).     Temp: {temp}
                (___(__)    Max-Min Temp: {max} - {min}
                 * * * *    Hum: {nem}
                 * * * *    WndSpd: {hiz}

             """).format(desc=desc, name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

    sis = ("""

             _ - _ - _ -    {name}({desc})
             _ - _ - _      Temp: {temp}
             _ - _ - _ -    Max-Min Temp: {max} - {min}
                            Hum: {nem}
                            WndSpd: {hiz}

             """).format(desc=desc, name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

    yok=("""

                  |===\      {name}({desc})
                  |    |     TempTemp: {temp}
                  | * *|     Max-Min Temp: {max} - {min}
                  |  | |     Hum: {nem}
                  |-//-|     WndSpd: {hiz}
                  ------

                 """).format(desc=desc, name=name, temp=temp, max=maxt, min=mint, hiz=hiz, nem=nem)

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
