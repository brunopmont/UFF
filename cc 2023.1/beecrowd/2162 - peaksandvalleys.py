n = int(input())
path = []
final = 0
path = list(map(int, input().split()))
if n == 1:
        final = 1
elif n == 2:
    if path[0] != path[1]:
        final = 1
    elif path[0] == path[1]:
        final = 0
else:
    for i in range(1, n-1):
        if path[i-1] < path[i] and path[i] > path[i+1]:
            final = 1
        elif path[i-1] > path[i] and path[i] < path[i+1]:
            final = 1
        elif path[i] == path[i-1] or path[i] == path[i+1]:
            final = 0
            break
        else:
            final = 0
            break
print(final)