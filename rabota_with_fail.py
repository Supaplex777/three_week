import csv
#Задание
#Создайте список словарей:
#       [
#      {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
#     {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
#    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#]
#Запишите содержимое списка словарей в файл в формате csv

message = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]


with open ('fail.csv', 'w', encoding='utf = 8', newline='') as test: 
    fields = ['name','age','job']
    writer = csv.DictWriter(test,fields,delimiter='-')
    writer.writeheader()
    for a in message:
        writer.writerow(a)


