#У вас есть список чисел. 
#Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым

numbers = [5, 8, 12, 3, 7]

while numbers:
    removed = numbers.pop(0)
    print("Element deleted:", removed)
    print("Current list:", numbers)


# Как сделать это же задание со строкой: напишите цикл, который выводит на экран и «удаляет» первый символ строки,
# пока она не станет пустой?

text = "My honesty setting is at 90%"

while text:
    removed = text[0]
    print("Removed character:", removed)
    text = text[1:]
    print("Current string:", text)


# Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького 
# до самого большого, пока он не останется пустым.

numbers = [7, 2, 5, 1, 9, 3]

while numbers:
    min_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i

    print("Element deleted:", numbers[min_index])
    del numbers[min_index]
    print("Current element:", numbers)

