n = int(input())
val = []
for i in range(n):
    p, g = map(float, input().split())
    preal = p/g * 1000
    val.append(preal)
print('{:.2f}'.format(min(val)))