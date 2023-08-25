x = list(str(input()))
if x.count('1') % 2 == 0:
    x.append('0')
else:
    x.append('1')
print(''.join(x))