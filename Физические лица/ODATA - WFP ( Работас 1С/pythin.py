import re
from socket import gaierror  
import requests

print('1 шаг - чтение данных с 1С')
username="Администратор"
password='rO2hemab'
r = requests.get('http://185.246.89.41/WFP_DEMO/odata/standard.odata/Catalog_ФизическиеЛица?$format=application/json', auth=(username.encode('utf-8'),password.encode('utf-8'))) 

print('2 шаг - запись в текстовый файл')
f = open('text.txt', 'w')
f.write(str(r.text))
f.close

print('3 шаг - сортировка данных')
max = 80
min = 4
find_kirill=''
f = open('text.txt')
sort =open('sort.txt','w')
for line in f:
    if (len(line) < max) and (len(line) > min):
        
        sort.write(line[1:-2]+'\n')

f.close
sort.close
f = open('text.txt', 'r+')
f.truncate()       
print('4 шаг - запись в бд')