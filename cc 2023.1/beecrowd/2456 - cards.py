conj = list(map(int, input().split()))
stts = 'N'
for i in range(1, 4):
    if conj[i] > conj[i-1] and conj[i+1] > conj[i]:
        stts = 'C'
    elif conj[i] < conj[i-1] and conj[i+1] < conj[i]:
        stts = 'D'
    elif conj[i] < conj[i-1] and conj[i+1] > conj[i]:
        stts = 'N'
        break
    elif conj[i] > conj[i-1] and conj[i+1] < conj[i]:
        stts = 'N'
        break
print(stts)