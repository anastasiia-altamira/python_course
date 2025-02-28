# Задача 3
# Пользователь вводит целое число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарём, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.


s = int(input())

if (s % 4 == 0 and s % 100 != 0) or (s % 400 == 0):
    print("YES! It's a leap year")
else:
    print("NO! It's a common year")

