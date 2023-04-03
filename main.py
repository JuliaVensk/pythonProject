# name = input()
# age = input()
# print(f"Hello, my name is {name}, I am {age} years old.")
# print(1, 2, 3, 4, sep="!", end="?")
# print("hello")
# text = 'Hello world'
# text1 = "Hello world"
# text2 = """Hello world
# 111
# wow
# """
# print(text2)
# text3 = input()
# print(text3)
# name = "Samantha"
# surname = "Smith"
# balance = 2000
# print(f"Dear {name} {surname}, your balance is {balance - 500} pounds")
# user_name = input()
# print(f"Hello {user_name}!")
# user_name = "Julia"
# print(f"Hello {user_name}!")
# input("Hello world")

# num1 = 12
# num2 = 7
# print(num1 + num2)
# print(num2 - num1)

# num1 = int(input())
# num2 = int(input())
# print(f"result = {num1 +num2}")

# print("*********")
# print("*       *")
# print("*       *")
# print("*********")

# print(89//15)
# print(17 - 45//8)
# print(100/2**2)
# print(16**0.5)
# print(round(1/3,2))
# t = 0
# z = 50
# d = z - 15
# # z = 2 * d
# # t = z - 40
# # # print(t)
# p = 5
# y = 7
# w = p + y
# w = w + 1
# p = y
# y = 10
# p = 2 + w + y
# print(p)
# a = 7
# a = a + a
# a = a + a + a
# print(a)
# a = float(input("side a : "))
# b = float(input("side b : "))
# c = float(input("side c : "))
# p = a + b + c
# print(p)
# x = 3
# print(x < 4 or not x > 6)
# print(x < 5 or not x > 1)
# a = 2
# if a != 5:
#     print("right")
# elif a > 5:
#     print("well done")
# else:
#     print("wrong")

# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a, b)
# print(type(a), type(b))

# a, b, c = map(int, input().split())
# print(a, b, c, sep=",")
# a, b, c, d, f = map(int, input().split())
# print(max(a, b, c, d, f))
# n, a, b = map(int, input().split())
# s = (a*b) * 2 * n
# print(s)
# message = 0
# if message:
#     print(message)
# else:
#     print("you string is empty")
# num = 5
# if num%2:
#     print("нечетное")
# else:
#     print("четное")
# s = "hello world"
# # print(s.replace("e", "?"))
# print("£".join(s))

# a = int(input("any digit: "))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f"{a} devides by 2 and 10")
#     else:
#         print(f"{a} devides by 2, but not 10")
# else:
#         print(f"{a} doesn't devides by 2")

# hero = int(input())
# if hero <= 0:
#     print("False")
# else:
#     print("True")

# num = int(input())
# if num % 2:
#     print("Нечетное")
# else:
#     print("Четное")

# text = input()
# i = 1
# while i < 5:
#     print(text)
#     i +=1

# num1 = str(input())
# operator = str(input())
# num2 = str(input())
# result = num1
# print(f"{num1} {operator} {num2} = {result}")

# n = int(input())
# print(n-1, "<", n, "<", n+1, sep='')

# text1 = ("Да прибудет")
# text2 = ("с тобой")
# text3 = ("Cила")
# print(text1,"---",text2,"---", text3, sep='', end="")

# a = input()
# print(1, 2, 3, 4, 5, sep=a)

# text = input()
# text2 = "Сказала она"
# print(text, "-", text2)

# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')

# a = int(input())
# print(a//1000)

# n = int(input())
# r = int(input())
# print(n//r)

# n = int(input())
# a = n//100
# # print(a)
# b = (n - a*100)//20
# # print(a + b)
# c = (n-(a*100+b*20))//10
# # print(a + b + c)
# d = (n-(a*100+b*20+c*10))//5
# # print(a +b +c + d)
# e = n-(a*100+b*20+c*10+d*5)
# print(a + b + c + d + e)

# def greet():
#     return"hello world!"
# print(return)

# d = (n-c)//5
# e = n - d
# print(a + b + c + d + e)

# num1 = int(input("Number1: "))
# num2 = int(input("Number2: "))
# operator = input("Operator: ")
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
#  if num2 == 0 and operator == "/":
#         try:
#             result = num1 / num2
#             print(f'Result = {result}')
#         except ZeroDivisionError:
#             print("На ноль делить нельзя")
# else

# text = "Hello"
# i = 0
# while i < 6:
#     print(i, text)
#     i += 1
#
# text = "Hello"
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, text)
# a = 2
# b = 3
# a, b = b, a
# print( a, b)

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])

# my_list1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(sum(my_list1))
#
# # list1 = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# list2 = [20, 15, 8, 7, 6]
# power = list(map(lambda x: x**2, list2))
# # filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, list1))
# # print(*filtered)
# # power = list(map(lambda x: x**2 if isinstance(x, int), list1))
# print(power)

# for modules import Hello
# print(modules.Hello ('Sam'))

# def fun():
#     s = 'hi'
#     print(f' First {s}')
# s = 'hello'
# fun()
# print(f' Second {s}')

# def multi():
#     x = 10
#     y = 5
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
# multi()
# a, b, *c = [1, 'hello', 3.5, True]
# # print(a, b, c)
# def fun(a, b, c):
#     print(a, b, c)
# a = (True, 51, 'Hello', (1, 2,))

# def fun(*args):
#     s = 0
#     print(args)
#     for i in args:
#         s += i
#     print(s)
# fun (1, 4, 7, 19, 10, 12)
# def return_dict(*args, **kwargs):
#     print(kwargs)
#     print(args)
# return_dict(1, 2, 3, a=2, b=4, c=6)
# a = [34, 67, 2, 54, 9]
# # a.sort(key = lambda x: x % 2 == 0)
# print(sorted(a, key = lambda  x: x % 2 == 0))
# # print(a)
# a = '1 2 3 4 5'
# b = list(map(str, a.split()))
# print(b)

# def count_consonants(text):
#     text1 = set(text.lower())
#     l =[]
#     for i in text1:
#         if i not in 'aeiou' and i.isalpha():
#             l.append(i)
#     return len(l)
#
# print(count_consonants('ergrehttrhyy  tyjyj  tj8o645f  rtert'))
#
# def alias_gen(f_name, l_name):
#     if f_name[0].isalpha() or l_name[0].isalpha:
#         return f'{FIRST_NAME.get(f_name[0].title())} {SURNAME.get(l_name[0].title())}'
#     return "Your name must start with a letter from A - Z."

def add(a, b):
    return a + b








