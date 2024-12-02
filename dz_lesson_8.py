print("             Задание №1")
# Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы

import time

# Декоратор для измерения времени выполнения
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Время начала выполнения
        try:
            result = func(*args, **kwargs)
        except RecursionError:
            raise  # Пробрасываем дальше для обработки
        finish = time.perf_counter()  # Время окончания выполнения
        return finish - start  # Возвращаем только время выполнения
    return wrapper

# Функции факториала с декоратором
@time_decorator
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@time_decorator
def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Ввод числа
while True:
    try:
        number = int(input("Введите число для вычисления факториала (неотрицательное): "))
        if number < 0:
            raise ValueError("Число должно быть неотрицательным.")
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте снова.")

# Обычная функция
iterative_time = factorial_iterative(number)

# Генератор
generator_time = factorial_generator(number)

# Рекурсия
try:
    rec_start = time.perf_counter()
    recursive_result = factorial_recursive(number)
    rec_finish = time.perf_counter()
    recursive_time = rec_finish - rec_start
except RecursionError:
    recursive_time = None
    

# Вывод времени выполнения
print(f"Время выполнения (обычная функция): {iterative_time:.6f} секунд")
print(f"Время выполнения (генератор): {generator_time:.6f} секунд")
print(f"Время выполнения (рекурсия): {recursive_time:.6f} секунд" if recursive_time is not None else "Ошибка: превышение глубины рекурсии")


print("             Задание №2. Декоратор")
# Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:

# @typed(type='str')
# def add_two_symbols(a, b):
#     return a + b
#
# add_two_symbols("3", 5) -> "35" 
# add_two_symbols(5, 5) -> 55 
# add_two_symbols('a', 'b') -> 'ab'
#
# @typed(type='int')
# def add_three_symbols(a, b, c):
#     return a + b + c
#
# add_three_symbols (5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001

def typed(type: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Определяем соответствующий тип
            if type == "str":
                check_type = str
            elif type == "int":
                check_type = int
            elif type == "float":
                check_type = float

            # Преобразуем позиционные аргументы
            converted_args = []
            for arg in args:
                if type == "str":
                    converted_args.append(str(arg))
                elif type == "int":
                    converted_args.append(int(arg))
                elif type == "float":
                    converted_args.append(float(arg))

            # Преобразуем именованные аргументы
            converted_kwargs = {}
            for key, value in kwargs.items():
                if type == "str":
                    converted_kwargs[key] = str(value)
                elif type == "int":
                    converted_kwargs[key] = int(value)
                elif type == "float":
                    converted_kwargs[key] = float(value)

            # Вызываем оригинальную функцию с преобразованными аргументами
            return func(*converted_args, **converted_kwargs)

        return wrapper

    return decorator


@typed(type="str")
def add_two_symbols(a, b):
    return a + b


@typed(type="float")
def add_three_symbols(a, b, c):
    return a + b + c


# Тестирование
print(add_two_symbols("3", 5))       # "35"
print(add_two_symbols(5, 5))         # "55"
print(add_two_symbols('a', 'b'))     # "ab"

print(add_three_symbols(5, 6, 7))    # 18.0
print(add_three_symbols("3", 5, 0))  # 8.0
print(add_three_symbols(0.1, 0.2, 0.4))  # 0.7000000000000001

print("             Задание №3. Лексиграфическое возрастание")
# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19). 
# Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке. 
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре встречается позже слова three, 
# а слово three - позже слова оnе (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)

# number_names = {
#               0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:'five', 
#               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
#                12: 'twelve',13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
#                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen
#                }

number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
input_numbers = input("Введите числа от 0 до 19, разделенные пробелом (не более 100): ").split()
try:
    input_numbers = [int(num) for num in input_numbers]
    for num in input_numbers:
        if num < 0:
            raise ValueError(f"Ошибка: число {num} меньше 0")
        if num > 19:
            raise ValueError(f"Ошибка: число {num} больше 19")
    if len(input_numbers) > 100:
        raise ValueError("Введено более 100 чисел.")
    sorted_numbers = sorted(input_numbers, key=lambda x: number_names[x])
    print("Числа в порядке лексикографической сортировки их названий: ")
    print(" ".join(map(str, sorted_numbers)))
except ValueError as err:
    print(f"Ошибка: {err}")

