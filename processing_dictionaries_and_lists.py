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

































