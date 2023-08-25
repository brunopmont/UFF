n = int(input())
for i in range(n):
    text = list(map(str, input().split()))
    for j in range(len(text)):
        print(text[j][0], end='')
    print()