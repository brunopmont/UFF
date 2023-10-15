h1, m1, h2, m2 = map(int, input().split())
h, m = 0, 0
while not h1==m1==h2==m2==0:
    if h1 == h2:
        if m1 == m2:
            h = 24 * 60
            m = 0
        elif m1 > m2:
            h = 24 * 60
            m = m2 - m1
        else:
            h = 0
            m = m2 - m1
    if h2 < h1:
        h = (24 - h1 + h2) * 60
        if m1 == m2:
            m = 0
        elif m1 > m2:
            m = m2 - m1
        else:
            m = m2 - m1
    if h2 > h1:
        h = (h2 - h1)*60
        if m1 == m2:
            m = 0
        elif m1 > m2:
            m = m2 - m1
        else:
            m = m2 - m1
    print(h+m)
    h1, m1, h2, m2 = map(int, input().split())