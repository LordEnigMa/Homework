# mytuple = (1, 2, 3, 4, ('Hello World!', 'Hello'))

# for i in mytuple:
#       if isinstance(i, tuple):
#             break
#       print(i)



# mytuple = (1, 2, 3, 4, ('Hello World!', 'Hello'), True)
# mytuple = reversed(mytuple)

# for i in mytuple:
#       print(i)



# mytuple = (1, 2, 3, 4, ('Hello World!', 'Hello'))
# length = 0

# for i in mytuple:
#       length += 1

# print(length)



# mytuple = ('n', 11, 'good', 3, ('Hello', 'World!'))
# res = ''

# for i in mytuple:
#       if isinstance(i, int):
#             i = str(i)
#             res += i
#       elif isinstance(i, str):
#             res += i
#       elif isinstance(i, tuple):
#             for j in i:
#                   res += j
      
# print(res)



# mytuple = (15, 12, 13)
# res = 0

# for i in mytuple:
#       res += i  
      
# print(res)



# mytuple = (111, 'hello', 'world', True, 228)
# find = input('Введите слово: ')
# res = False

# for i in mytuple:
#       if find == str(i):
#             print('Такое слово есть.')
#             break
#       else:
#             res = False

# if(res == False):
#       print('Такого слово нету.')



# mytuple = (15, 25, 4, 60, 77, 1)
# max =  mytuple[0]
# min = mytuple[0]

# for i in mytuple:
#       if max < i:
#             max = i
#       if min > i:
#             min = i
            
# print(max, min)