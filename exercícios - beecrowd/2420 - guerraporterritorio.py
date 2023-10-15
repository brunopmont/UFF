n = int(input())
sec = list(map(int, input().split()))
totsec = sum(sec)/2
som = 0
i = 0
while som != totsec:
    som = som + sec[i]
    i += 1
print(i)