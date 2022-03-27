# mydict = {
#       'A': 25,
#       'B': 77,
#       'C': 15,
#       'D': 49
# }
# mylist = []

# for i in mydict.values():
#       mylist.append(i)
# mylist.sort()
# for i in mylist:
#       print(i, end=' ')



# mydict = {
#       'A': 25,
#       'B': 77,
#       'C': 15,
#       'D': 49
# }
# mydict['E'] = 78



# mydict = {
#       'A': 25,
#       'B': 77,
#       'C': 15,
#       'D': 49
# }

# key = input('Введите ключ: ')
# for i in mydict:
#       if key in i:
#             print('Такой ключ есть!')
# else:
#       print('Такого ключа нету!')



# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)



# mydict = {
#       'A': 10,
#       'B': 14,
#       'C': 8
# }
# res = 1

# for i in mydict.values():
#      res *= i
# print(res)



# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# res = sorted(mydict.values(), reverse=True)
# res = res[:3]
# print(res)

# for x, y in zip(mydict.keys(), res):
#       if x in mydict.keys() and y in mydict.values():
#             print(str(x) + ': ' + str(y),end=', ')



# words = input('Введите 2 слова: ')
# words = words.split(' ')
# res = 0

# if len(words[0]) == len(words[1]):
#       for i in words[0].upper():
#             if words[0].upper().count(i) == words[1].upper().count(i):
#                   res += 1
#       if res == len(words[0]):
#             print('Эти два слова анаграммы!')
#       else:
#             print('Эти два слова не анаграммы!')