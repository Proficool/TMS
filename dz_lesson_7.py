print("             Задание №1")
# 1. Создать lambda функцию, которая принимает на  вход имя и выводит его в формате "Hello, {name}"

greet = lambda name: f"Hello, {name}"
name = input("Введите имя: ")
print(greet(name))

print("             Задание №2")
# 2. Создать lambda функцию, которая принимает на вход список имен и выводит их в формате "Hello, {name}" в другой список 

greet_list = lambda names: [f"Hello, {name}" for name in names]
names = input("Введите список имен через запятую: ").split(",")
names = [name.strip() for name in names]  
greetings = greet_list(names)
print("Список приветствий:", greetings)

print("             Задание №3")
# 3. Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6,-12.7] 
# и возвращает новый список только с положительными числами 

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, -12.7]
positive_numbers = (num for num in numbers if num > 0)
result = list(positive_numbers)
print("Положительные числа:", result)

print("             Задание №4")
# 4. Необходимо составить список чисел которые указывают на длину слов в строке: 
# sentence = "thequick brown fox jumps over the lazy dog", но только если слово не "the" с обработкой исключений

sentence = "thequick brown fox jumps over the lazy dog"
sentence_list = sentence.split()
lengths = []
for word in sentence_list:
    try:
        if word == "the":
            raise ValueError(f"Слово содержащее'{word}' исключено из обработки.")  
        lengths.append(len(word)) 
    except ValueError as e:
        print(e)  
print("Длины слов не содержащих 'the'):", lengths)