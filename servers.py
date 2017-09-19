# -*- coding: utf-8 -*-

import requests, re, sys # импорт библиотек 

n = 0 # index list

x = 1 # number page

# list url 
url2 = 'http://gamingservers.ru/minecraft/?page=' #присвоение переменным значений.
url3 = 'http://gamingservers.ru/css/?page='
url4 = 'http://gamingservers.ru/cs1.6/?page='
url5 = 'http://gamingservers.ru/sanandreas/?page='
url6 = 'http://gamingservers.ru/mta/?page='
url7 = 'http://gamingservers.ru/rust/?page='
url8 = 'http://gamingservers.ru/left4dead2/?page='
url9 = 'http://gamingservers.ru/teamfortress2/?page='
url10 = 'http://gamingservers.ru/dayzmod/?page='
url11 = 'http://gamingservers.ru/garrysmod/?page='
url12 = 'http://gamingservers.ru/7daystodie/?page='
url13 = 'http://gamingservers.ru/halflife2dm/?page='
url14 ='http://gamingservers.ru/halflife/?page='
url15 = 'http://gamingservers.ru/killingfloor/?page='
url16 = 'http://gamingservers.ru/battlefield4/?page='
url17 = 'http://gamingservers.ru/dayofdefeatsource/?page='
url18 = 'http://gamingservers.ru/callofduty4/?page='
url19 = 'http://gamingservers.ru/quake3/?page='
url20 = 'http://gamingservers.ru/ark/?page='
url21 = 'http://gamingservers.ru/arma2/?page='
url22 = 'http://gamingservers.ru/arma3/?page='
url23 = 'http://gamingservers.ru/battlefield3/?page='
url24 = 'http://gamingservers.ru/cscz/?page='
url25 = 'http://gamingservers.ru/dayofdefeat/?page='
url26 = 'http://gamingservers.ru/left4dead/?page='
url27 = 'http://gamingservers.ru/quake2/?page='
url28 = 'http://gamingservers.ru/quake4/?page='
url29 = 'http://gamingservers.ru/zombiepanic/?page='
url30 = 'http://gamingservers.ru/jc2/?page='
url31 = 'http://gamingservers.ru/ventrilo/?page='
url32 = 'http://gamingservers.ru/teamspeak3/?page='
mas = [url2,url3,url4,url5,url6,url7,url8,url9,url10]
mas += [url11,url12,url13,url14,url15,url16,url17,url18,url19]
mas += [url20,url21,url22,url23,url24,url25,url26,url27,url28,url29]
mas += [url30,url31,url32] # добавление переменных в массив .
# list url 
'''
banner= '* : PROGECT GAMINGSERVER.RU [LIST SERVER] : *'
print(banner)
url = 'http://gamingservers.ru'
req = requests.get(url) # отправка get запроса.
print '='*len(banner) # выводит длину переменной.
status = req.status_code # получаем код.(ответ).
if status == 200: # сверяем с 200
  print('[+] STATUS CODE : '+str(status)+' : '+'IT ALL OK')
if status != 200:
 print('[+] STATUS CODE : '+str(status)+' : '+':( SORRY') # правельней ставить else .
 sys.exit() # завершаем процесс .
''' # комментарии
while True:
 while n < len(mas)+1:
    print '!!!!!!!!!!!!!!!!'+str(n)+'!!!!!!!!!!!!!!!!'+str(x)
    req = requests.get(mas[n]+str(x))
    text = req.content
    find = re.findall(r'title="RU"></a>(.*?)</td>',text)
    if len(find) > 0:
       for line in find:
         print str(line)
         f = open('servers','a')
         f.write(str(line)+'\n')
       f.close()
       x += 1
       continue
    if len(find) == 0:
       x = 1
       n += 1
       continue
