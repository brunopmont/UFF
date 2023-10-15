a, b, c = map(int, input().split())
maiorab = int((a + b + abs(a - b)) / 2)
maior = int((maiorab + c + abs(maiorab - c)) / 2)
print("{} eh o maior".format(maior))