notes = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32 , 'X': 1/64}
seq = list(input().split('/'))
while '*' not in seq:
    size = 0
    certo = 0
    seq.remove('')
    seq.remove('')
    for i in range(len(seq)):
        size = 0
        for j in range(len(seq[i])):
            size = size + float(notes.get(seq[i][j]))
        if size == 1:
            certo += 1
    print(certo)
    seq = list(input().split('/'))