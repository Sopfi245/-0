my_string = input("Введите текст: ")
print("Количество символов:", len(my_string))
print("Строка в верхнем регистре:", my_string.upper())
print("Строка в нижнем регистре:", my_string.lower())
no_spaces_string = my_string.replace(" ", "")
print("Строка без пробелов:", no_spaces_string)
print("Первый символ:", my_string[0])
print("Последний символ:", my_string[-1])
