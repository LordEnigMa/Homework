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

# class MyClass:

#       def __init__(self, mylist):
#             self.mylist = list(mylist)

#       def max_length(self):
#             mylist = self.mylist
#             max_length = 0

#             for i in mylist:
#                   if len(i) > max_length:
#                         max_length = len(i)
            
#             return max_length
      
#       def longest_strings(self):
#             max_length = self.max_length()
#             new_list = []

#             for i in self.mylist:
#                   if len(i) == max_length:
#                         new_list.append(i)
            
#             print(new_list)

# instance = MyClass(["aba", "aa", "ad", "vcd", "aba"])
# instance.longest_strings()

############################################

# def Lucky(n):
      
#       if len(str(n)) % 2 == 0:
#             length = len(str(n)) // 2
#             n = str(n)
#             part1 = n[:length]
#             part2 = n[length:]
#             sum1 = 0
#             sum2 = 0

#             for i in part1:
#                   sum1 += int(i)
#             for i in part2:
#                   sum2 += int(i)
            
#             if sum1 == sum2:
#                   print('Счастливый билет!')
#             else:
#                   print('Не счастливый билет!')

#       else:
#             print('Не счастливый билет!')

# Lucky(1230)

############################################

def sort_by_height(mylist):
      new_list = []
      indexes = []

      for i in range(len(mylist)):
            if int(mylist[i]) != -1:
                  new_list.append(int(mylist[i]))
            else:
                  indexes.append(int(i))

      new_list.sort()

      for i in indexes:
            new_list.insert(i, -1)

      print(new_list)

sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180])