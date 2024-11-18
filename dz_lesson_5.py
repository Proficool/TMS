# url = "www.my_site.com#about"
# updated_url = url.replace("#", "/")
# print(updated_url)

def update_url():
    url = "www.my_site.com#about"
    return url.replace("#", "/")
print(update_url())


# word = "stroka"
# new_word = word + "ing"
# print(new_word)

def add_ing_to_word():
    word = "stroka"
    return word + "ing"
print(add_ing_to_word())


# colors = ["red", "blue", "green", "yellow", "purple"]
# print(colors[1])

colors = ["red", "blue", "green", "yellow", "purple"]
def get_second_element(colors):
    return colors[1]
print(get_second_element(colors))  


