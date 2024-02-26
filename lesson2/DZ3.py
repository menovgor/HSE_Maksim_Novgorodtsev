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


#Создайте функцию для генерации текста с адресом суда.
from data_for_lesson2 import courts, respondents
def make_court_nominative_case(court_name: str) -> str:
    """

    :param court_name:
    :return:
    """
    words = court_name.split(" ")[2::]
    text = "Арбитражный суд"
    for i in words:
        text += f" {i}"
    return text


def make_a_header(court, plaintiff, respondent):
    text = f"-------------------------------\n" \
           f"В {make_court_nominative_case(court['court_name'])}\n" \
           f"Адрес: {court['court_address']}\n\n" \
           f"" \
           f"Истец: {plaintiff['name']}" \
           f"ИНН {plaintiff['inn']} ОГРНИП {plaintiff['ogrnip']}\n" \
           f"Адрес: {plaintiff['address']}\n\n" \
           f"" \
           f"Ответчик: {respondent['short_name']}”\n" \
           f"ИНН {respondent['inn']} ОГРН {respondent['ogrn']}\n" \
           f"Адрес: {respondent['address']}\n\n" \
           f"" \
           f"Номер дела {respondent['case_number']}\n"
    return text