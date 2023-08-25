n = int(input())
nin = 0
nout = 0
for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        nin += 1
    else:
        nout += 1
print("{} in".format(nin))
print("{} out".format(nout))