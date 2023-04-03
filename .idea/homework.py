# homework lecture 3
# 1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']  print  1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])
# или
# list1 = my_list[2]
# print(*list1, sep='\n')

# 2. list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100] total sum and print all strings with "a"
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])

# 3. list ['cat', 'dog', 'horse', 'cow'] turn to tuple
# list1 = ['cat', 'dog', 'horse', 'cow']
# print(tuple(list1))

# 4. программа, определ , какая семья больше; прогр. имеет 2 input(), членов семьи пеечислить через
#  запятую. Результат - прогр выводит семью с БОльшим кол-вом, если одинак, то "Equal"
# family_1 = tuple(input('Введите текст через запятую: ').split(','))
# family_2 = tuple(input('Введите текст через запятую: ').split(','))
# if len(family_1) == len(family_2):
#  print('Equal')
# elif len(family_1) > len(family_2):
#  print('family_1')
# else:
#  print('family_2')

# 5. create dict Film with keys - title, director, year, budget, main_actor, slogan.
# #     в значение можно передать инфо о ыильме. print a) only keys, b) only value, c) both
# film = {'title': 'Green mile', 'director': 'Mr Smith', 'year': 1997, 'budget': '1000000$'}
# print(film.keys())
# print(film.values())
# print(film)

# 6. Найдите сумму всех значений в словаре
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# 7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(list_1))

# 8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'},
#     set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# a = set1.intersection(set2)
# print(a)
# b = set1.symmetric_difference(set2)
# print(b)
# print(set1.issubset(set2))
# print(set2.issubset(set1))
#
# LECTURE 4
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
#
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.








