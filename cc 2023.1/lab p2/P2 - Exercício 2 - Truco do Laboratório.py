cards = {}
n = int(input())
dic = {1:8, 2:9, 3:10, 4:1, 5:2, 6:3, 7:4, 11:6, 12:5, 13:7}
tim, maia = 0, 0
a, b = 0, 0
for i in range(n):
    a, b = 0, 0
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    if dic[a1] >= dic[b1]:
        a += 1
    else:
        b += 1
    if dic[a2] >= dic[b2]:
        a += 1
    else:
        b += 1
    if dic[a3] >= dic[b3]:
        a += 1
    else:
        b += 1
    if a > b:
        tim += 1
    elif a < b:
        maia += 1
print('{} {}'.format(tim, maia))