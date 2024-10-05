# Пустотелый квадрат
size = 10

for i in range(size):
    if i == 0 or i == size - 1:
        print('*' * size)
    else:
        print('*' + ' ' * (size - 2) + '*')


# Заполненный квадрат
size = 10

print("\n")
for i in range(size):
    print('*' * size)
