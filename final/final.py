"""
1. Напишите функцию fib(), которая будет генерировать числа в последовательности
Фибоначчи и принимать в качестве аргумента целое число, обозначающее номер
числа в последовательности, на котором следует остановиться.
* Задание «со звёздочкой» (повышенной сложности): сделайте функцию-генератор,
используя yield.
    """
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


"""
2. Напишите функцию-конвертер из системы римских цифр в знакомую нам десятичную
целочисленную.
"""

def roman_to_usual_numbers(roman):
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    final_value = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_numbers[char]
        if value < prev_value:
            final_value -= value
        else:
            final_value += value
        prev_value = value

    return final_value

"""
3. Монотонная последовательность — это последовательность, элементы которой с
увеличением номера только возрастают, или, наоборот, только убывают.
Массив nums является монотонно возрастающим, если верно i <= j, nums[i] <= nums[j].
Напишите функцию, которая будет принимать в себя массив, состоящий из цифр, и
возвращать:
 true — если массив является монотонным,
 false — в обратном случае.
"""


def monoton(nums):
    monoincrease = True
    monodecrease = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            monoincrease = False
        if nums[i] > nums[i - 1]:
            monodecrease = False

    return monoincrease or monodecrease
