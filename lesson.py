# Основы языка PYTHON 3/2

# Присвоение переменным значений.

p = 1
# Название переменной через = присваеваем значение.
p += 2
print(p)  # Выведет 3 так как мы прибавили к переменной p через += двойку (Сумма)

s = 1, 2, 2, 1, 2, 22
sum = sum(s) # Функция для суммирования чисел !
print(sum)
 # Деление, Умножение и т.д

ppp = 1000000/34 # Деление .
uuu = 1000000*3 # Умножение .
mmm = 11111%5 # Незнаю что делает но помню такое.
ooo = 10000+121 # Сумма чисел .
aaa = 10000-124 # Вычитание чисел .

###

array = [] #  Создали пустой массив .
array = [1, 2, 3, 4, 5, 6, "Leha"] # Создали массив .
        #0, 1, 2, 3, 4, 5,   6 (ИНДЕКС) ПЕРЕЧЕСЛЕНИЕ НАЧИНАЕТСЯ С 0.
print(array[0])  # Что выведет ? В Python 3 обязательно надо ставить скобки при print .
print(array[1])  # Что выведет ?
print(array[2])  # Что выведет ?
print(array[-1]) # Что выведет ?
print(array[1::4])  # Что выведет ?
print(array[2:4]) # Что выведет ?
array.append(555) # Добовляем в массив число 555 !
print(array) # Что выведет ?

dict = {"Name": "Лешка", "Pol": "Мужской", "Age": 17}  # Список (dict)
name = dict.get("Name")  # get мы обращаемся к названию под-списка так сказать и оно выводит сожержимое.
pol = dict.get("Pol")
age = dict.get("Age")

print("Имя: {}, Пол: {}, Возраст: {} лет .".format(name, pol, age))  # Вывод переменной name,pol,age с помощью format.
#Кстати ковычки могут быть одинарными и двойными (',").
print("Имя: "+name+", Пол: "+pol+", Возраст: "+str(age)+" лет .")  # Можно вывести так просто преплюсовав ! Но так медленее.
# Можно вывсти с помощью % . Но тоже медлено .

number = 1 # INT Обычное число . Их в python длина может достигать очень больших размеров .
print(str(number) + " : Type : "+str(type(number)))
tuple = 1, 2, 3, 4, 'p'  # TUPLE # Кортэж .
print(str(tuple) + " : Type : "+str(type(tuple)))
bool = True # BOOL , True и False (1,0) # Логические значения .
print(str(bool) + " : Type : "+str(type(bool)))
float = 1.1 # FLOAT # числа с плавающей точкой
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
# Выведет поочереди каждое имя в именах.
for n in range(0,1000): # xrange(1000)
   print(n)
# Логично выведет все числа попорядку от 0 до 1000

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

# => - Равно или больше,
# <= - Меньше или равно,
# > - Больше,
# < - Меньше.
# Существуют еще and, or, not.

if name or name_2 == 'Henry':
# Если им или имя 2 равно генри то выполняем то что ниже 
    print('Henry')
if name and name_2 == 'Lola','Emma':
# Если имя и имя 2 равны Лола и Эмма то выполняем то что ниже
    print(name+' : '+name_2)
if 'Amanda' not in name:
# Если Amanda нет в name то выполняем код ниже :)
    print('Amanda not found')
else: # В пративном случае ничего не делаем.
    pass # Кстати pass ничего не делает !

import random # импорт модуля random
from random import randint  # можно импортировать только тот модуль из библиотеки который нужен,
from random import randint as rint # и обзывать как тебе угодно через as (переводится - как).
# для random имопртируем randint как rint (На руском :))
r_n = random.randint(0, 10) # randint делает рандомное число от 0 до 10
r_n_2 = rint(0, 1)

# Исключения ! ( Обработка ошибок).

try:
    a = a # Специально присвоил переменной a несуществующую переменную a.
except Exception as e:
    print(e) # Выводит ошибку .

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

from urllib.request import Request,urlopen # импортируем 2 модуля
from re import findall # Можно с помощью BS # импортируем 1 модуль
url = "http://spaces.ru/" # надеюсь ясно
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"} # User-Agent 
Req = Request(url=url,headers=headers) # Добавляет в запрос заголовок User-Agent
htmltext = urlopen(Req).read().decode() # Соендиняемся получаем и декодируем текст в utf-8 по стандарту
find = findall(r'<title>(.*?)</title>',htmltext) # ищем текст между двумя тэгами в htmltext
for f in find: # для каждой f в find принтуем f
        print(f)
# Все проще простого дальше некуда ...............

# print ('--'*34)

# Перечесляю модули которыми больше всего пользуюсь.
# urllib - Работа с http и https протоколами .
# random - Генерация рандомных чисел .
# argparse - Создание аргументов .
# sys - Системный можуль . Для закрытия процесса и т.д
# requests - Работа тоже с http, https протоколоами .
# time - Работа со временем .
# datetime - Тоже со временем но удобнее и лучше . Настоящее время .
# matplotlib - Работа с графиками .
# socket - Для работы с udp, tcp, icmp и т.д протоколами. Короче для работы с сетью .
# os - Работа с процессами и т.д .
# subprocess - Работа с процессами .
# math - Математическая библиотека . Например косинусы синусы арктангенсы логарифмы и т.д .
# json - Работа со списками в формате json .
# ast - Использую для преобразования из string в dict и т.д .
# smtplib Работа с smtp протоколом (почта). Старое pop3 .
# base64 - Шифрование base64.
# urllib2 - Работа с http, https протоколоми, но более сложна и детальна.
# hashlib - Всякие методы шифрования (md5, sha1) и т.д .
# threading - Множественное выполнение одной функции (задачи).
# PyQt5 - Графическая оболочка . GUI
# calendar - Обычный календарик .
# struct - IN/OUT Encrypt Decrypt .
# pprint - Просто для красивого вывода .
# numpy - Работа с массивами и много другого.
# scipy - Предназначена для математических вычислений .
# Tkinter - Тоже GUI популярная для linux, unix и т.д системах.
# vk - Библиотека написанная для VK_API .
# bs4 - Библиотека BeautifulSoup .
# socketserver - Почти тоже что и socket .

# Настал момент для ООП ( Обьектно-Ориентированный-Язык программирования или Обьектно Ориентированное Программирование).

class opt: создание обьекта (класс)
    def MyName(self): создание функции которая тоже обьект и принимает self обязательно.
        print('My name is Dasha !') # Вывод чего либо

o = opt() # Присвоение переменной opt(). ОБЬЕКТ.
o.MyName() # Выполняем функцию в обьекте (вызываем).

# Можно писать так opt().MyName()

class opt_2:
    def __init__(self,name,age): # инитиализируящая функция .
        self.name = name
        self.age = age
    def person_info(self):
        print ('My name is '+self.age+', and me '+str(self.age)+'year :)')

o = opt_2('Alex',17)
o.person_info()

# С этим разобрались !

# проверка имени функции (__name__ == '__main__')

def main(): Создаем функцию с именем main
    print('Hey BRO !')

if __name__ == '__main__': # Проверка если имя функции main то она точно будет запущена .
    main() Запускаем функцию .

# Работа с вводом выводом ...

inp = input('Введите пожалуйста ваше имя : ') # В python 2 (raw_input)

print ('Ваше имя : ' + inp)

# Работа с файлами..

#f1 = open('name_file.txt','mode')
def read_file(file):
   f1 = open(file,'r') # Открываем файл на чтение ('r').
   text = f1.read() # Читает текст из файла.
   print(text)
   f1.close() # Закрывает файл.
 
read_file('name_file.txt')
 
def write_text(file,text):
   f1 = open(file,'a') # Открывает файл на запись 'w', 'a' На все .
   f1.write(text+'\n') # Записываем в файл .
   f1.close() # Закрываем .

write_text('name_file.txt', 'Hello, World')

# Посчитаем сколько високосных годов было c 0 года в Юлианском календаре. Напишем грамотно .

from sys import exit
from datetime import date

def get_yevi(i,mas,year):
    while i < year:
      mas.append(i)
      i += 4
     return(len(mas))
     
i = 0
mas = []
year = date.today().year # Получаем сейчашний год.

number = get_yevi(i,mas,year) 
print(number)

exit(1)

# Проще некуда !

# 505 

# Теперь мы можем использовать это как наш модуль !

from year import get_yevi # Импорт нашего модуля .

i = 0
mas = []
year = date.today().year

number = get_yevi(i,mas,year) 
print(number)

# Вот написал сегодня игру в отгадывания дверей как играли с вами :)
# https://github.com/Elllender/list/blob/master/3doors.py
