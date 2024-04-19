'''
1. Сгенерируйте с использованием функции range (случайный шаг от 3 до 5)
массив, содержащий отсортированные числа от 10 до 250 млн.
Можно использовать функцию randomint из модуля random для ещё большей
рандомизации значений, но для целей работы алгоритма бинарного поиска
проследите, чтобы значения в массиве были отсортированы.
2. Сгенерируйте с помощью list comprehensions и функции randomint
(встроенный модуль random) 10 случайных чисел.
3. Напишите функцию для алгоритма линейного поиска.
4. Напишите функцию для алгоритма бинарного поиска.
5. Проверьте наличие ранее сгенерированных случайных чисел в массиве с
помощью алгоритмов линейного и бинарного поиска, замерьте время'''
import random
import time

# Генерация массива
start = 10
end = 250000000
step = random.randint(3, 5)
array = list(range(start, end + 1, step))

# Функция для генерации 10 случайных чисел
random_numbers = [random.randint(start, end) for _ in range(10)]


# Функция для линейного поиска
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


# Функция для бинарного поиска
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Проверка наличия чисел в массиве и замер времени
for num in random_numbers:
    start_time = time.time()
    linear_result = linear_search(array, num)
    linear_time = time.time() - start_time

    start_time = time.time()
    binary_result = binary_search(array, num)
    binary_time = time.time() - start_time

    print(f"Число {num}:")
    print(
        f"Линейный поиск: {'Найдено на индексе ' + str(linear_result) if linear_result != -1 else 'Не найдено'} Время: {linear_time} секунд")
    print(
        f"Бинарный поиск: {'Найдено на индексе ' + str(binary_result) if binary_result != -1 else 'Не найдено'} Время: {binary_time} секунд")
    print()