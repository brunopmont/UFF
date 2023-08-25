na = int(input())
nb = int(input())
nc = int(input())
gt = [0, 0, 0]
gt[0] = 2 * nb + 4 * nc
gt[1] = 2 * na + 2 * nc
gt[2] = 4 * na + 2 * nb
print(min(gt))