p = [4.00, 4.50, 5.00, 2.00, 1.50]
x, y = map(int, input().split())
print('Total: R$ {:.2f}'.format(p[x-1] * y))