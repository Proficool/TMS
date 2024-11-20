func_1 = lambda a : a * a
print(func_1(5))

func_2 = lambda a, b : a + b
print(func_2(2,5))

func_3 = lambda *args : args + args
print(func_3(1,2,3,4))

func_3 = lambda **kwargs : kwargs
print(func_3(a = 1, d =2))

def greatings(hello):
    return hello()
def hello():
    return 1
print(greatings(hello))

my_dict = {"a": 1, "b": 2, "c": 3}
values_iterator = iter(my_dict.values())
for value in values_iterator:
    print(value)

my_gen = a