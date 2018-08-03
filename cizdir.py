def load(veri):
    desc = veri[1]
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
