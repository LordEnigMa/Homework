# from math import ceil

# class MyClass:
      
#       def __init__(self, year):
#             self.year = year

#       def to_century(self):
#             if self.year > 0 and self.year <= 100:
#                   print('Первый век.')
#             elif self.year < 1:
#                   print('Введите положительное число.')
#             else:
#                   if self.year % 100 == 0:
#                         print(self.year // 100)
#                   else:
#                         print(self.year // 100 + 1)

# instance = MyClass(2022)
# instance.to_century()

############################################

# class MyClass:

#       def ispolidrom(self):
#             string = input('Введите слово: ')
                  
#             if len(string) > 1 and len(string) < 106:
#                   reversed_string = string[-1::-1]
                  
#                   if string == reversed_string:
#                         print('Это слово полидром.')
#                   else:
#                         print('Это слово не полидром.')
#             else:
#                   print('Неправильный ввод!')

# inst = MyClass()
# inst.ispolidrom()

############################################

# class MyClass():
      
#       def __init__(self):
#             self.string = input('Введите элементы списка через пробел: ')

#       def max(self):
#             mylist = self.string.split(' ')
#             Max = int(mylist[0]) * int(mylist[1])

#             for i in range(2, len(mylist) - 1):
#                   if int(mylist[i]) * int(mylist[i+1]) > Max:
#                         Max = int(mylist[i]) * int(mylist[i+1])
            
#             print(Max)

# inst = MyClass()
# inst.max()

############################################

