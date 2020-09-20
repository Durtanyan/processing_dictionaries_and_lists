'''
Даны 2 словаря account и user со следующей структурой:

Структура словаря “account”:
ключ 1: “login”. Тип значения: строка
ключ 2: “password”. Тип значения: строка

Словарь “user”:
ключ 1: “name”. Тип значения: строка;
ключ 2: “age”. Тип значения: число;
ключ 3: “account”. Тип значения: словарь account.
'''

'''
ЗАДАЧА:
1. Создать 4 переменные account1, account2, account3, account4 типа 
словарь со структурой 'account'. Значения ключей для переменных:

account1: login - ivan, password - q1;
account2: login - petr, password - q2;
account3: login - olga, password - q3;
account4: login - anna, password - q4.


2. Создать 4 переменные user1...user4 типа словарь со структурой “user”. 
Значения ключей для переменных:

user1: name - Иван, age - 20, account - account1;
user2: name - Петр, age - 25, account - account2;
user3: name - Ольга, age - 18, account - account3;
user4: name - Анна, age - 27, account - account4.


3. Создать список user_list, состоящий из 4 элементов - user1...user4
'''

# 1. Создать 4 переменные account1, account2, account3, account4 
# типа словарь со структурой “account”.
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# 2. Создать 4 переменные user1...user4 типа словарь со структурой “user”
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

# 3. Создать список user_list, состоящий из 4 элементов - user1...user4
user_list = [user1, user2, user3, user4]

'''
1. Программа должна запрашивать у пользователя ключ и выдавать информацию
 обо всех пользователях по введенному ключу, независимо от того 
 в каком регистре введено значение маленькими или большими буквами. 
 Если такого ключа нет, программа должна выдавать сообщение:
 “Введенный ключ не найден”. 

Сообщение для ввода ключа (input): “Введите ключ (name или account): ”

Пример работы программы:

Введите ключ (name или account): NaMe
значение ключа name для юзера 1 = Иван
значение ключа name для юзера 2 = Петр
значение ключа name для юзера 3 = Ольга
значение ключа name для юзера 4 = Анна
'''

value_name_or_account = input('Введите ключ (name или account): ')
#убираем пробелы справа и слева у введенного значения
value_name_or_account = value_name_or_account.strip()

#преобразовываем введенное строковое значение к нижнему регистру
value_name_or_account = value_name_or_account.lower()

#вводим счетчик итераций
count = 1

#основной цикл программы
if value_name_or_account == 'name' or value_name_or_account == 'account':
    for i in user_list:
        print(' Значение ключа ' + value_name_or_account + ' для юзера ' + str(count) + ' = ' + i['name'])
        count += 1
else:
    print(' Введенный ключ не найден.')
    
    

#print(value_name_or_account)

































