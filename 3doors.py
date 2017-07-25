import sys
from random import shuffle,choice

rooms = ['', '', 'car'] # Создание массива

shuffle(rooms) # Рандомно упорядочивает значения в массиве .

# Присвоение переменным (дверям) значений массива.

room1 = rooms[0]
room2 = rooms[1]
room3 = rooms[2]

# print (rooms)

inp = int(input('[+] Введите номер двери из ' +str(len(rooms))+ ' дверей : ')) # Говорит само за себя

# Дальше идут сплошные условия ...

if inp == 1:
    if room1 == '':
        n_1 = rooms.index('car')+1 # Получаем по содержимому номер в массиве и плюсуем 1 чтобы получить номер двери
        vrfy_1 = input('[+] Вы хотите поменять свой выбор между дверью {} и {} (yes,no) ? '.format('1',str(n_1)))
        if vrfy_1 == 'yes':
            print('[+] Вы отгодали дверь !')
        if vrfy_1 == 'no':
            print('[-] Вы не отгодали дверь !')
    if room1 == 'car':
        n_1 = 2,3
        r_1 = choice(n_1) #Рандомно выбирает между 2 и 3 .
        vrfy_1 = input('[+] Вы хотите поменять свой выбор между дверью {} и {} (yes,no) ? '.format('1',str(r_1)))
        if vrfy_1 == 'yes':
            print('[-] Вы не отгодали дверь !')
        if vrfy_1 == 'no':
            print('[+] Вы отгодали дверь !')
if inp == 2:
    if room2 == '':
        n_1 = rooms.index('car')+1
        vrfy_1 = input('[+] Вы хотите поменять свой выбор между дверью {} и {} (yes,no) ? '.format('2',str(n_1)))
        if vrfy_1 == 'yes':
            print('[+] Вы отгодали дверь !')
        if vrfy_1 == 'no':
            print('[-] Вы не отгодали дверь !')
    if room2 == 'car':
        n_1 = 1,3
        r_1 = choice(n_1)
        vrfy_1 = input('[+] Вы хотите поменять свой выбор между дверью {} и {} (yes,no) ?'.format('2',str(r_1)))
        if vrfy_1 == 'yes':
            print('[-] Вы не отгодали дверь !')
        if vrfy_1 == 'no':
            print('[+] Вы отгодали дверь !')
if inp == 3:
    if room3 == '':
        n_1 = rooms.index('car')+1
        vrfy_1 = input('[+] Вы хотите поменять свой выбор между дверью {} и {} (yes,no) ? '.format('3',str(n_1)))
        if vrfy_1 == 'yes':
            print('[+] Вы отгодали дверь !')
        if vrfy_1 == 'no':
            print('[-] Вы не отгодали дверь !')
    if room3 == 'car':
        n_1 = 2,3
        r_1 = choice(n_1)
        vrfy_1 = input('[+] Вы хотите поменять свой выбор между дверью {} и {} (yes,no) ? '.format('3',str(r_1)))
        if vrfy_1 == 'yes':
            print('[-] Вы не отгодали дверь !')
        if vrfy_1 == 'no':
            print('[+] Вы отгодали дверь !')
else:
    pass
        
    

