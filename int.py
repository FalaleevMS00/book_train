#Напишите функцию pos_add(a, b),
# которая возвращает положительное значение сложения двух целых чисел.
def pos_add(a, b):
    return abs(a + b)

#Определите функцию foo(a),
# которая возвращает результат целочисленного и по модулю деления любого целого числа на -11.
def foo(a):
    return (a // -11, a % -11)

print(pos_add(1, 3))
print(foo(22))