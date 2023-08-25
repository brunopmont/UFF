a, b, c = map(float, input().split())
res = 0
if c > a:
    res = a
    a = c
    c = res
if b > a:
    res = a
    a = b
    b = res
if c > b:
    res = c
    c = b
    b = res
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")