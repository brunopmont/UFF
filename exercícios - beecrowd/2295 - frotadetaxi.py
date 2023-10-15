a, g, ra, rg = map(float, input().split())
pg = g / rg
pa = a / ra
if pg > pa:
    print('A')
elif pa > pg:
    print('G')
elif pa == pg:
    print('G')