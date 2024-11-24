# Импорт модуля os
import os

print("             Задание №1")
# 1. Дан файл целых чисел, содержащий не менее четырех элементов. 
# Вывести первый, второй, предпоследний и последний элементы данного файла. Если чисел меньше 3 выводить ошибку. 

# Запрос числа с проверкой
while True:
    count = int(input("Сколько чисел вы хотите ввести? (не менее 4): "))
    if count >= 4:
        break
    print("Ошибка: число должно быть не менее 4. Попробуйте снова.")

filename = f"numbers_{count}.txt"

# Создание файла с числами
with open(filename, "w") as file:
    for i in range(count):
        number = input(f"Введите число {i + 1}: ")
        file.write(number + " ")

# Чтение данных из файла
with open(filename, "r") as file:
    numbers = file.read().strip().split()

print("Первый элемент:", numbers[0])
print("Второй элемент:", numbers[1])
print("Предпоследний элемент:", numbers[-2])
print("Последний элемент:", numbers[-1])

# Удаление файла
os.remove(filename)
print(f"Файл '{filename}' был удален.")

print("             Задание №2")
# 2. Дан файл целых чисел. Создать два новых файла, первый из которыx содержит четные числа из исходного файла, 
# а второй - нечетные( в том же порядке). Если четные или нечетные числа в исходном файле отсутствуют, то соответствующий 
# результирующий файл оставить пустым. 

# Запрос желаемого количества чисел
count = int(input("Сколько чисел вы хотите ввести? "))
filename = f"numbers_{count}.txt"

with open(filename, "w") as file:
    for i in range(count):
        number = input(f"Введите число {i + 1}: ")
        file.write(number + " ")

# Создание файлов для четных и нечетных чисел
even_filename = "even_numbers.txt"
odd_filename = "odd_numbers.txt"

with open(filename, "r") as file:
    numbers = list(map(int, file.read().strip().split()))

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

with open(even_filename, "w") as even_file:
    even_file.write(" ".join(map(str, even_numbers)))

with open(odd_filename, "w") as odd_file:
    odd_file.write(" ".join(map(str, odd_numbers)))

# Вывод результатов
print("Четные числа:", even_numbers if even_numbers else "Нет четных чисел")
print("Нечетные числа:", odd_numbers if odd_numbers else "Нет нечетных чисел")

# Удаление файлов
os.remove(filename)
os.remove(even_filename)
os.remove(odd_filename)

print("Все файлы были удалены.")

print("             Задание №3")
# 3. Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

# Создание файла с вещественными числами
filename = "float_numbers.txt"
numbers = input("Введите вещественные числа через пробел: ").split()
numbers = [float(num) for num in numbers]

# Записываем числа в файл
with open(filename, "w") as file:
    file.write(" ".join(map(str, numbers)))

# Чтение из файла, замена чисел их квадратами и вывод результата
with open(filename, "r") as file:
    numbers = list(map(float, file.read().split()))
    squared_numbers = [num ** 2 for num in numbers]

# Перезапись файла с квадратами
with open(filename, "w") as file:
    file.write(" ".join(map(str, squared_numbers)))

# Чтение из файла и вывод результата
with open(filename, "r") as file:
    updated_numbers = file.read()

print("Содержимое файла с квадратами чисел: " + updated_numbers)

# Удаляем файл
os.remove(filename)
print(f"Файл '{filename}' удален.")

print("             Задание №4")
# 4. Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа.

# Шаг Создаем два файла с текстом
with open("file1.bin", "wb") as file1:
    file1.write("Text_1".encode())  # Запись в бинарном формате

with open("file2.bin", "wb") as file2:
    file2.write("Text_2".encode())  # Запись в бинарном формате

# Читаем содержимое файлов
with open("file1.bin", "rb") as file1:
    content1 = file1.read().decode()  # Чтение и преобразование из байтов в строку

with open("file2.bin", "rb") as file2:
    content2 = file2.read().decode()  # Чтение и преобразование из байтов в строку

# Пишем содержимое одного файла в другой
with open("file1.bin", "wb") as file1:
    file1.write(content2.encode())  # Преобразуем строку в байты и записываем

with open("file2.bin", "wb") as file2:
    file2.write(content1.encode())  # Преобразуем строку в байты и записываем

# Выводим содержимое измененных файлов
with open("file1.bin", "rb") as file1:
    updated_content1 = file1.read().decode()  # Чтение и преобразование из байтов в строку

with open("file2.bin", "rb") as file2:
    updated_content2 = file2.read().decode()  # Чтение и преобразование из байтов в строку

print(f"Содержимое файла file1.bin: {updated_content1}")
print(f"Содержимое файла file2.bin: {updated_content2}")

# Удаляем созданные файлы
os.remove("file1.bin")
os.remove("file2.bin")

print("Все созданные файлы удалены.")