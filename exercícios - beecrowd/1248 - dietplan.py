n = int(input())
for i in range(n):
    diary = list(input())
    b = list(input())
    l = list(input())
    for i in range(len(b)):
        if b[i] in diary:
            diary.remove(b[i])
        else:
            diary.append('CHEATER')
    for i in range(len(l)):
        if l[i] in diary:
            diary.remove(l[i])
        else:
            diary.append('CHEATER')
    if 'CHEATER' in diary:
        print('CHEATER')
    else:
        print(''.join(sorted(diary)))