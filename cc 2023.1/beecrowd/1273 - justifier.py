n = int(input())
while n != 0:
    words = []
    char = 0
    for i in range(n):
        x = input()
        words.append(x)
        if len(x) > char:
            char = len(x)
    for i in range(n):
        print('{}'.format(words[i].rjust(char)))
    n = int(input())
    if n != 0:
        print()