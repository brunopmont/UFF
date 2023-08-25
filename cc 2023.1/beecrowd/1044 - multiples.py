a, b = map(int, input().split())
if a >= b:
    if a % b == 0:
        print("Sao Multiplos")
    elif a % b != 0:
        print("Nao sao Multiplos")
elif a < b:
    if b % a == 0:
        print("Sao Multiplos")
    elif b % a != 0:
        print("Nao sao Multiplos")