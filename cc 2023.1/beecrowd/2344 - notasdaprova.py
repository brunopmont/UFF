n = int(input())
if n == 0:
    print('E')
elif 1 <= n and n <= 35:
    print('D')
elif 36 <= n and n <= 60:
    print('C')
elif 61 <= n and n <= 85:
    print('B')
elif n >= 86:
    print('A')