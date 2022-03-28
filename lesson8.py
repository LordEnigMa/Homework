# pcs = ['Hp', 'Asus', 'Dell', 'Mac', 'Lenovo']
# if 'Mac' in pcs:
#       print(True)



# chars = ('!', '@', '#', '$', '%', '&', '*')

# while True:
#       password = input('Введите пароль: ')
#       symbol_count = 0
#       number_count = 0
      
#       if len(password) > 7:
#             for symbol in chars:
#                   if password.count(symbol) > 0:
#                         symbol_count += password.count(symbol)
#             for number in password:
#                   if number.isdigit():
#                         number_count += 1
#             if  symbol_count < 2:
#                   print('Повторите попытку!')
#                   continue
#             if number_count < 2:
#                   print('Повторите попытку!')
#                   continue
#             print('У вас сложный пароль!')
#             break
#       else:
#             print('Повторите попытку!')



# url = 'http://www.youtube.com/watch?v=2282aUSw5vU'
# url = url.split('http://www.youtube.com/watch?v=')
# url = ''.join(url)
# print(url)



# word = input('Введите слово: ')
# mylist = []

# for i in word:
#       mylist.append(i)
      
# mylist.reverse()
# mylist = ''.join(mylist)

# if word == mylist:
#       print('Это слово полиндром.')
# else:
#       print('Это слово не полиндром.')



# string = 'Hello World!'
# string = string.split(' ')
# print(string)



# numbers = input('Введите 5 чисел через пробел: ')
# numbers = numbers.split(' ')
# even_numbers = ''

# for i in numbers:
#       if int(i) % 2 == 0:
#             even_numbers += i
#             even_numbers += ' '
# print(even_numbers)



# import random as r

# names = ['Liam', 'Noah', 'Olivia', 'Emma', 'Mark']

# for i in range(0, 5):
#       current = r.choice(names)
#       print(current)
#       names.remove(current)



# mylist = [11, 25, 34, 34, 15, 16, 15]

# for i in mylist:
#       if mylist.count(i) > 1:
#             while mylist.count(i) > 1:
#                   mylist.remove(i)
                  
# print(mylist)