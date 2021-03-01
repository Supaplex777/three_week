#Скачайте файл по ссылке
#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt



##word = 0
   #for text in my_file: # прочел
       # print(text)
       # word =word +len(text)
       # print(word)


#with open ('referat.txt','w',encoding='utf-8') as my_file:
   # my_file = my_file.replace('.','!')
    #print(my_file)
#with open ('referat2.txt','a',encoding='utf-8') as my_file_2:
    ## my_file_2.write(line)



with open ('referat.txt','r+',encoding='utf-8') as my_file:
    test = my_file.read()
    print(test)
    print(len(test))
    test1 = test.replace('.','!')
    print(test1)

with open ('refarat2.txt','w',encoding='utf-8') as a:
    print(a.write(test1))

   
 
   

