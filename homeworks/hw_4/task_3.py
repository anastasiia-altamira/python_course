# Задача 3
# Напишите функцию, которая удаляет все небуквенные символы внутри строки (ограничимся латинским алфавитом). 
# Проверьте, что вы правильно закодили с помощью инструкции assert.


import re

special_string = "spe@#$ci87al\*&"
print("Строка до преобразования: ", special_string)

normal_string = re.sub("[^A-Za-z]", "", special_string)
print("Строка после преобразования: ", normal_string)

assert normal_string == "special", "В строке недопустимые символы"
