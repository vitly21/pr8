a = 0
while a == 0:
    print("Введите целые числа c и b")
    c = input()
    b = input()
    if isinstance(c, int) and isinstance(b, int):
        g = c + b
        print(f"Их сумма равна {g}")
    else:
        print("Введенное число некоректно")
        break
