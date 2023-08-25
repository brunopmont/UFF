a, b, c = map(float, input().split())
per = 0
area = 0
if c + b > a > abs(c - b) and a + c > b > abs(a - c) and a + b > c > abs(a - b):
    per = a + b + c
    print("Perimetro = {:.1f}".format(per))
else:
    area = (a + b) * c / 2
    print("Area = {:.1f}".format(area))
    