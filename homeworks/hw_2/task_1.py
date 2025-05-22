# 1.Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)

s = "123"
is_integer = s.isdigit()
print(is_integer)

# 2. Посчитайте сколько у вас пробелов в строке.
# 3. Посчитайте сколько у вас символов точки '.' в строке.

s = 'Text .with. several. spaces. and. dots.   '
spaces_count = s.count(' ')
dots_count = s.count('.')
print("Number of spaces in the string:", spaces_count)
print("Number of dots in the string:", dots_count)

# 4. Создайте строку "Homework". Преобразуйте её в строку длиной 100 символов, посередине которой исходное слово,
#  а с обоих сторон строка заполнена пробелами. Выведите её на экран.

word = "Homework"
centered_word = word.center(100)
print(centered_word)

# 5. Сделайте первые буквы слов строки большими (upper case).

text = "сделайте первые буквы слов строки большими"
result = text.title()
print(result)