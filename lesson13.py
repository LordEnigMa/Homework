# f = open('text.txt', 'r')
# res = f.read()
# res = res.split(', ')
# mydict = {}
# for i in res:
#       mylist = i.split(',')
#       a = mylist[0].index('-') + 1
#       user_login = mylist[0][a:]
      
#       del mylist[0]
      
#       a = mylist[0].index('-') + 1
#       user_password = mylist[0][a:]
      
#       mydict[user_login] = user_password

# login = input('Введите логин: ')
# password = input('Введите пароль: ')

# for x, y in zip(mydict.keys(), mydict.values()):
#       if login == x and password == y:
#             print('Правильные данные!')
#             break
# else:
#       print('Неправильный логин или пароль!')