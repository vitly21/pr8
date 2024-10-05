import math

def is_number(value):
    try:
        float(value)  
        return True
    except ValueError:
        return False

print("Введите два числа: ")
a_input = input()
b_input = input()

if is_number(a_input) and is_number(b_input):
    a = math.floor(float(a_input))
    b = math.floor(float(b_input))

    for i in range(a+1, b):
        print(i)
else:
    print("Ошибка! Введите корректные числа.")
