n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
vnorep = [v[0]]
for i in range(1, n):
    if v[i] != v[i-1]:
        vnorep.append(v[i])
print(len(vnorep))