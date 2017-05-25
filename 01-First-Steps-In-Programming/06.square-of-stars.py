n = int(input())
rows = n - 2
print('*' * n)
for i in range(0, rows):
    print('*' + ' ' * rows + '*')
print('*' * n)
