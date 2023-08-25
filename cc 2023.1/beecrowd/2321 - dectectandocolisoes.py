col = 0
ax0, ay0, ax1, ay1 = map(int, input().split())
bx0, by0, bx1, by1 = map(int, input().split())
i = ax0
j = ay0
while i <= ax1 and col != 1:
    while j <= ay1 and col != 1:
        if bx0 <= i <= bx1:
            if by0 <= j <= by1:
                col = 1
        else:
            break
        j += 1
    i += 1
print(col)