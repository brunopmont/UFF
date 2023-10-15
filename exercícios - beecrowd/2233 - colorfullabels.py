import math

hexastr = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
hexaint = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
quoc = []

def convert(x):
    conv = 0
    for i in range(len(x)):
        valor = hexastr[x[len(x)-1-i]]
        conv = conv + valor*(16**i)
    return conv
    
rh = list(input())
ri = convert(rh)
gh = list(input())
gi = convert(gh)
bh = list(input())
bi = convert(bh)

red = 1
green = (math.floor(int(ri) / int(gi)))**2
blue = green * (math.floor(int(gi) /int(bi)))**2

tot = red + green + blue
totmut = tot

while totmut > 16:
    quoc.append(totmut % 16)
    totmut = totmut // 16
quoc.append(totmut)
quoc = quoc[::-1]
for i in range(len(quoc)):
    quoc[i] = hexaint[quoc[i]]
print(''.join(quoc))