'''
Сразу пишу что есть языки низкоуровневые, прикладные, высокоуровневые,сверхвысокоуровневые.
Так что этот язык сверхвысокоуровневый (дальше проще некуда, как написано в вики не как сделать ? а что сделать ? отвечает на вопрос данный язык .)
Сразу пишу чтоб все тщательно просмотрел и хоть что-то понял пока меня не будет или пока я буду !!! Можешь распечатать и читать , если чего непонятно, обезательно набирай код в repl.it (сайт)  смотри результат, разбирайся !!!
'''

# Основы основ языка PYTHON 3/2

# Присвоение переменным значений.

p = 1
# Название переменной через = присваеваем значение.
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
array.append(555) # Добовляем в массив число 555 !
print(array) # Что выведет ?

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
# urllib - Работа с http и https протоколами .
# random - Генерация рандомных чисел .
# argparse - Создание аргументов .
# sys - Системный можуль . Для закрытия процесса и т.д
# requests - Работа тоже с http, https протоколоами .
# time - Работа со временем .
# datetime - Тоже со временем но удобнее и лучше . Настоящее время .
# matplotlib - Работа с графиками .
# socket - 
# os - Работа с процессами и т.д .
# subprocess - Работа с процессами .
# math - Математическая библиотека .
# json - Работа со списками в формате json .
# ast - Использую для преобразования из string в dict и т.д .
# smtplib Работа с smtp протоколом (почта). Старое pop3 .
# base64 - Шифрование base64.
# urllib2 - Работа с http, https протоколоми, но более сложна и детальна.
# hashlib - Всякие методы шифрования (md5, sha1) и т.д .
# threading - Одновременное выполнение одной функции.
# PyQt5 - Графическая оболочка .
# calendar - Обычный календарик .
# struct - IN/OUT Encrypt Decrypt .
# pprint - Просто для красивого вывода .
# numpy - Работа с массивами и много другого.
# scipy - Предназначена для математических вычислений .

Настал момент для ООП ( Обьектно-Ориентированный-Язык программирования).

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