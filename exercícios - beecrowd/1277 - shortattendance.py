t = int(input())
for i in range(t):
    c = 0
    n = int(input())
    names = list(input().split())
    att = list(input().split()) 
    for i in range(n):
        medfreq = 75/100*(att[i].count('A') + att[i].count('P'))
        if att[i].count('P') < medfreq:
            if c == 0:
                print('{}'.format(names[i]), end='')
            else:
                print(' {}'.format(names[i]), end = '')
            c = 1
    print('', end='\n')