# Присвоение переменным значений !

p = 1
# Название переменной через = присваеваем значение !
p += 2
print(p)  # Выведет 3 так как мы прибавили к переменной p через += двойку (Сумма)

s = 1, 2, 2, 1, 2, 22
sum = sum(s) # Функция для суммирования чисел !
print(sum)

array = [1, 2, 3, 4, 5, 6, "Leha"] # Создали массив !
        #0, 1, 2, 3, 4, 5,   6 (ИНДЕКС) ПЕРЕЧЕСЛЕНИЕ НАЧИНАЕТСЯ С 0.
print(array[0])  # Что выведет ?
print(array[1])  # Что выведет ?
print(array[2])  # Что выведет ?
print(array[1::4])  # Что выведет ?

dict = {"Name": "Лешка", "Pol": "Мужской", "Age": 11}  # Список (dict)
name = dict.get("Name")  # get мы оюращаемся к названию под списка так сказать и оно выводит сожержимое.
pol = dict.get("Pol")
age = dict.get("Age")

print("Имя: {}, Пол: {}, Возраст: {} лет .".format(name, pol, age))  # Вывод переменной name,pol,age с помощью format.
print("Имя: "+name+", Пол: "+pol+", Возраст: "+str(age)+" лет .")  # Можно вывести так просто преплюсовав ! Но так медленее.

number = 1 # INT
print(str(number) + " : Type : "+str(type(number)))
tuple = 1, 2, 3, 4, 'p'  # TUPLE
print(str(tuple) + " : Type : "+str(type(tuple)))
bool = True # BOOL , True и False (1,0)
print(str(bool) + " : Type : "+str(type(bool)))
float = 1.1 # FLOAT
print(str(float) + " : Type : "+str(type(float)))  # Вывод переменной float и Типа переменной float с помощью type. str() - Это функция преобразовывает из int в string формат.

# Комментарии начинаются с # В Python . и есть такие.
'''Приветик !!!
Как дела ?
'''

# циклы, условия

names = 'leha', 'pavel', 'anton'


# for
for name in names:
    print(name)

# while

i = 0
while i < len(names): # len() - получаем длину !
    print(i)
    i += 1

# if ,elif ,else, Короче условия !

name = 'Boby'
name_2 = 'Gabby'

if name == name_2: # == - это мы сверяем  (равно) , != знак неравенства (неравно).
    print('Имена совпадают.')
elif name != name_2:
    print('Имена не совпадают.')
else:
    print('Странная ситуация !')

import random # импорт модуля random
from random import randint  # можно импортировать только тот модуль из библиотеки который нужен,
from random import randint as rint # и обзывать как тебе угодно через as (переводится - как).
# для random имопртируем randint как rint (На руском :))
r_n = random.randint(0, 10) # randint делает рандомное число от 0 до 10
r_n_2 = rint(0, 1)

# Исключения ! ( Обработка ошибок).

try:
    a = a
except Exception as e:
    print(e)

# Функции !

def name_function(num,num_2):  # Принимает значения
    # name
    return num + num_2  # Возвращает сумму num и num_2
print(name_function(1, 20))

# Разные штуки с текстом !
text = 'Ala Beaa Huh'
split_text = text.split(' ') # rsplit ::: "Режет"
print(split_text)
replace_text = text.replace('A', 'H') # Заменяет
print(replace_text)
text.encode("utf-16") # Кодирования в utf-16 из utf-8 .deocode Декодирование.
print(text)
u_text = text.upper() # Приводит все к верхнему регистру !
l_text = text.lower() # Приводит все к нижнему регистру ! 
print(u_text)
print(l_text)
# И т.д

# Про ООП потом !

# Давай напишем простой скрипт для получения html разметки с сайта грубо говоря  и выведем то что находится между тэгами <title>awdawd</title>

from urllib.request import Request,urlopen
from re import findall # Можно с помощью BS
url = "http://spaces.ru/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
Req = Request(url=url,headers=headers)
htmltext = urlopen(Req).read().decode()
find = findall(r'<title>(.*?)</title>',htmltext)
for f in find:
        print(f)
# Все проще простого дальше некуда ...............

# print ('--'*34)

# Перечесляю модули которыми больше всего пользуюсь.
# urllib
# random
# argparse
# sys
# requests
# time
# datetime
# matplotlib
# socket
# os
# subprocess
# math
# json
# ast
# smtplib
# base64
# urllib2
# hashlib
# threading
# PyQt5
# calendar
# struct
# pprint
