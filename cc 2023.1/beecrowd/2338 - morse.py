n = int(input())
for z in range(n):
    morse = {'=.===':'a', '===.=.=.=':'b', '===.=.===.=':'c', '===.=.=':'d', '=':'e', '=.=.===.=':'f', '===.===.=':'g', '=.=.=.=':'h', '=.=':'i', '=.===.===.===':'j', '===.=.===':'k', '=.===.=.=':'l', '===.===':'m', '===.=':'n', '===.===.===':'o', '=.===.===.=':'p', '===.===.=.===':'q', '=.===.=':'r', '=.=.=':'s', '===':'t', '=.=.===':'u', '=.=.=.===':'v', '=.===.===':'w', '===.=.=.===':'x', '===.=.===.===':'y', '===.===.=.=':'z'}
    sentence = list(map(str, input().split('.......')))
    for i in range(len(sentence)):
        sentence[i] = list(map(str, sentence[i].split('...')))
    for i in range(len(sentence)):
        for j in range(len(sentence[i])):
            sentence[i][j] = morse[sentence[i][j]]
    for i in range(len(sentence)):
        if len(sentence) > 0:
            if i == len(sentence) - 1:
                print(''.join(sentence[i]), end='\n')
            else:
                print(''.join(sentence[i]), end=' ')
        else:
            print(''.join(sentence[i]), end='')