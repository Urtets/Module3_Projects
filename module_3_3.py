# Задача 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

b = 3
print_params(b = 25)
print(b)
print_params(c = [1,2,3])

# Задача 2
values_list = ["Каспер-Пёс", 1, "Белый"]
values_dict = {'a': 'Супер-Пёс', 'b': 1, 'c': 'Бишон'}

print_params(*values_list)
print_params(**values_dict)

# Задача 3
values_list_2 = ['Пёсель', 'Красавчик']
print_params(*values_list_2, 42)