# string = 'python 3.9'
# res = 0 

# for i in string:
#       if i.isdigit():
#             res += int(i)
            
# print(res)



# string = 'python 3.915'
# letCount = 0
# numCount = 0

# for i in string:
#       if i.isdigit():
#           numCount += 1
#       elif i != ' ' and i != '.':
#           letCount += 1

# print(numCount)
# print(letCount)



# import random as r

# user_point = 0
# pc_point = 0
# chars = ('Камень', 'Ножница', 'Бумага')

# while True:
#       if pc_point == 2 or user_point == 2:
#             print('Игра закончилась!')
#             break
#       user = input('Введите Камень или Ножница или Бумага: ')
#       pc = r.choice(chars)
#       if user == pc:
#             print('Ничья')
#             continue
#       elif (user == 'Камень' and pc == 'Бумага') or (user == 'Бумага' and pc == 'Ножница') or (user == 'Ножница' and pc ==  'Камень'):
#             pc_point += 1
#             print('ПК выиграл!')
#       elif (pc == 'Камень' and user == 'Бумага') or (pc == 'Бумага' and user == 'Ножница') or (pc == 'Ножница' and user ==  'Камень'):
#             user_point += 1
#             print('Вы выиграли!')
#       else:
#             print('Неправильный ввод, повторите попытку.')
#             continue
#       print('Очки пользователя: ', user_point)
#       print('Очки ПК: ', pc_point)



# list = [1, 20, True, (15, 20)]
# count = 0

# for n in list:
#       if isinstance(n, tuple):
#             break
#       count += 1

# print(count)



# list = [1, 20, True, (15, 20)]
# reverse = reversed(list)

# print(tuple(reverse))



# mytuple = (10, 20, 30)
# print(len(mytuple))

# length = 0
# for i in mytuple:
#       length += 1
      
# print(length)



# barer = input('Введите слова: ')
# barer = barer.split(' ')
# max = 0

# for i in range(len(barer)-1):
#       if len(barer[i]) > len(barer[i+1]):
#             max = barer[i]
#       elif len(barer[i]) == len(barer[i+1]):
#             max = barer[i]
#       else:
#             max = barer[i+1]
            
# print(max)



# list1 = ['asd', 112, 'hello', 56]
# list2 = ['world', 156, 'hello', 229]

# for i in list2:
#       if i in list1:
#             print(True)
#             break



# mydict = {
#       1: 25,
#       2: 37,
#       3: 110,
#       4: 5
# }

# mylist = []

# for i in mydict.values():
#       mylist.append(i)      
# mylist.sort()

# for i in mylist:
#       print(i, end=' ')



# string = 'Hello '
# mylist = []
# length = 0

# for i in string:
#       if i not in mylist:
#             mylist.append(i)

# print(len(mylist))


###############23.03.2022###############
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# res = []

# for i in a:
#       if i in b:
#             res.append(i)

# print(set(res))



# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []

# for i in a:
#       if i < 5:
#             res.append(i)

# print(res)


# mydict = {
#       'a':500,
#       'b':5874,  
#       'c': 56,
#       'd':400,  
#       'e':5874,
#       'f': 20
# }
# res = {}
# count = 0

# for i in mylist:
#       for x in mydict:
#             if i == mydict[x]:
#                   res.setdefault(x, i)

# mylist = sorted(mydict.values(), reverse=True)
# print(res)



# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# res = {}
# count = 0
# mylist = sorted(my_dict.values(), reverse=True)
# mylist = mylist[:3]


# for i in mylist:
#       name = 'asdfgh'
#       for x in my_dict:
#             if i == my_dict[x]:
#                   res.setdefault(x, i)
                  
# print(res)



# myset = {14, 15, 2, 999}
# for i in myset:
#       print(i)

# myset.add(228)
# myset.remove(14)

# x = 2
# if x in myset:
#       myset.remove(i)

from cowsay import cowsay

print(cowsay('Hello World'))