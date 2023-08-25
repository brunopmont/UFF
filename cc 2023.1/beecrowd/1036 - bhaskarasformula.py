a, b, c = map(float, input().split())
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Impossivel calcular")
elif a == 0:
    print("Impossivel calcular")
else:
    x1 = (- b + delta ** (1/2)) / (2 * a)
    x2 = (- b - delta ** (1/2)) / (2 * a)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))