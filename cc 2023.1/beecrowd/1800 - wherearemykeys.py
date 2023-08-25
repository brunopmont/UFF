q, e = map(int, input().split())
s = list(map(int, input().split()))
for i in range(q):
    x = int(input())
    if x in s:
        print('0')
    else:
        print('1')
        s.append(x)