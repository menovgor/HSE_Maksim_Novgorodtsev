# Функция вычисления факториала числа
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

# Функция поиска наибольшего числа из трех
def find_maximum_of_three(numbers):
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Функция расчета площади прямоугольного треугольника
def triangle_area(a, b):
    return 0.5 * a * b