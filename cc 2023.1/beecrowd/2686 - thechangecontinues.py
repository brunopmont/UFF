while True:
    try:
        M = float(input(""))
        t = 360 + 4 * M
        h = int(t // 60)
        m = int((t % 60) // 1)
        s = int((t - (h * 60 + m)) * 60)
        hor = ""
        if h >= 24:
            h = h - 24
        if 6 <= h < 12:
            hor = "Bom Dia!!"
        elif 12 <= h < 18:
            hor = "Boa Tarde!!"
        elif 18 <= h < 24:
            hor = "Boa Noite!!"
        elif 0 <= h < 6:
            hor = "De Madrugada!!"
        print(hor)
        print("{:0>2}:{:0>2}:{:0>2}".format(h, m, s))
    except EOFError:
        break
