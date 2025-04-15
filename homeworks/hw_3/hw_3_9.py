#Пишем программу, которая попросит пользователя ввести слово (строка без пробелов в середине, а вначале и в конце пробелы 
# могут быть). Пока он не введёт правильно, просите его ввести.

def remove_outer_spaces(s):
    while s and s[0] == ' ':
        s = s[1:]
    while s and s[-1] == ' ':
        s = s[:-1]
    return s

text = "   It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.   "
print("[" + remove_outer_spaces(text) + "]")  

