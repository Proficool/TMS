# url = "www.my_site.com#about"
# updated_url = url.replace("#", "/")
# print(updated_url)

def update_url():
    return url.replace("#", "/")
url = str(input("Введите url c решеткой : "))
print(update_url())

# word = "stroka"
# new_word = word + "ing"
# print(new_word)

def add_word2_to_word1(word1, word2):
    return word1 + word2
word1 = str(input("Введите слово 1 : "))
word2 = str(input("Введите слово 2 : "))
print(add_word2_to_word1(word1, word2))  


# colors = ["red", "blue", "green", "yellow", "purple"]
# print(colors[1])

def get_color(colors, n):

# Проверка, что индекс находится в пределах длины списка
    if 0 <= n < len(colors):
        return colors[n]
    else:
        return "Ошибка: индекс вне диапазона списка"

# Ввод списка цветов 
colors = input("Введите список цветов через запятую: ").split(",")

# Убираем лишние пробелы вокруг цветов
colors = [color.strip() for color in colors]

# Ввод номера цвета 
n = int(input(f"Введите номер цвета (0-{len(colors)-1}): "))

# Вывод выбранного цвета
print(f"Цвет под номером {n}: {get_color(colors, n)}")


