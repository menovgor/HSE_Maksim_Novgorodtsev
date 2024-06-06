

'''1. Задача о палиндроме.
Напишите функцию, которая будет принимать в себя тип данных int (число) и
возвращать тип bool, если переданное число является палиндромом.
Палиндром — слово, фраза или символы, которые одинаково читаются слева направо
и справа налево.'''
def palindrom(number: int) -> bool:
    str_number = str(number)
    # Сравниваем строку с её перевёртышем
    return str_number == str_number[::-1]

# Примеры
print(palindrom(454))
print(palindrom(-323))
print(palindrom(1000))
print(palindrom(45654))


'''2. Задача о сумме двух элементов массива.
Напишите функцию, которая в качестве аргументов принимает массив (list) с числами
и целевое число. Функция должна возвращать индексы элементов, которые в сумме
дают целевое число.'''

def two_elements_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return None

# Примеры
print(two_elements_sum([2, 7, 11, 15], 9))
print(two_elements_sum([3, 2, 4], 6))
print(two_elements_sum([3, 3], 6))
