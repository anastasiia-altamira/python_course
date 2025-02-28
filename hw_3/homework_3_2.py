# Задача 2
# Пользователь вводит строку. Разрежьте её на две части – равные, если длина строки чётная, а если длина строки нечётная, 
# то длина первой части должна быть на один символ больше. Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

s = input()
s_lenght = len(s)  
print("Lenght: ", s_lenght)  
s_left_side = ""  
s_right_side = ""  

if s_lenght % 2 == 0:
    s_middle_of_the_string = (s_lenght // 2) - 1 
else:
    s_middle_of_the_string = (s_lenght // 2) 

print("Middle of the string index: ", s_middle_of_the_string)  

s_left_side = s[:s_middle_of_the_string]  
s_right_side = s[s_middle_of_the_string:]  

print(s_right_side + s_left_side)  
