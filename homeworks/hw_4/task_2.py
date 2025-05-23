# Задание 2
#Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов. 
# Учитываем, что может быть повторяющиеся значения аргументов.

def second_smallest(*args):
    unique_values = sorted(set(args))
    if len(unique_values) < 2:
        print("Нет второго уникального значения")
    else:
        print(unique_values[1])
#second_smallest(1, 2, 3, 4, 5)
#second_smallest(5, 5, 5, 5)
second_smallest(1, 8, 8, 6, 9, 6)