print('Это калькулятор характеристик набора чисел.')
print('Введите набор чисел, разделяя числа пробелом.')
arr = [float(x) for x in input().split()]
a = 0
m = 0
r = 0
print('Что Вы хотите посчитать?')
print('Если необходимо, введите несколько чисел, не разделяя их дополнительными символами.')
print('1 - среднее арифметическое')
print('2 - медиана')
print('3 - размах')
req = input()
if '1' in req:
    a = round(sum(arr) / len(arr), 2)
    print('среднее арифметическое:', a)
if '3' in req:
    r = max(arr) - min(arr)
    print('размах:', r)
if '2' in req:
    arr_copy = arr
    arr_copy.sort()
    while len(arr_copy) > 2:
        arr_copy.pop(0)
        arr_copy.pop(-1)
    m = round(sum(arr_copy) / len(arr_copy), 2)
    print('медиана:', m)
