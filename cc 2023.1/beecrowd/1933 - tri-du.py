a, b = map(int, input().split())
c = 0
if a == b:
    c = a
elif a != b:
    if a >= b:
        c = a
    elif a < b:
        c = b
print(c)