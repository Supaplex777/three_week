

# Вывести последнюю букву в слове
word  =  'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
import collections
word2  =  'Архангельск'
c = collections.Counter(word2)
print(c)



# Вывести количество гласных букв в слове
word3  =  'Архангельск'
vowels = "аеёиоуыя"
for v in vowels:
    print(v, word3.lower().count(v))


# Вывести количество слов в предложении
предложение  =  'Мы приехали в гости'  
message = предложение.count(' ') + 1
print(message)
# ???


# Вывести первую букву каждого слова на индивидуальную строку
sentence = 'Мы приехали в гости'
list_slov = sentence.split()
for item in list_slov:
    print (item[0])
print('\n')


# Вывести усреднённую длину слова.
предложение  =  'Мы приехали в гости'
words = предложение.split()
average = sum(len(word) for word in words) / len(words)
print(average)
