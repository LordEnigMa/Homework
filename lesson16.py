# class MyClass:
#       def __init__(self, mylist):
#             self.mylist = list(mylist)            
#             self.mylist.sort()
      
#       def max(self):
#             print('Наибольшой элемент списка:', self.mylist[-1])
      
#       def min(self):
#             print('Наименьший элемент списка:', self.mylist[0])
      
#       def sum(self):
#             Sum = 0
            
#             for i in self.mylist:
#                   Sum += i
            
#             print('Сумма элементнов списка:', Sum)

# mylist = [12312, 12, 456, 451]
# instance = MyClass(mylist)
# instance.max()
# instance.min()
# instance.sum()

############################################

# class MyClass:
#       def __init__(self, mydict):
#             self.mydict = dict(mydict)
            
#       def max_values(self):
#             sorted_dict = {}
#             sorted_keys = sorted(self.mydict, key=self.mydict.get, reverse=True) 
            
#             for i in sorted_keys:
#                   if len(sorted_dict) == 2:
#                         break
#                   sorted_dict[i] = self.mydict[i]
                              
#             print('Два наибольших элемента словаря: ', end='')
#             for i in sorted_dict.values():
#                   print(i, end=' ')     
            
# mydict = {'a': 25, 'b': 14, 'c': 36}
# instance = MyClass(mydict)
# instance.max_values()

############################################

# import datetime

# class Parent:
#       def hello(self):
#             print('Hello World!')
      
#       def time(self):
#             time = datetime.date.today()
#             print(time)

# class Child(Parent):
      
#       def show(self):
#             super().hello()
#             super().time()

# instance = Child()

# instance.show()

############################################

# class Rectangle:
      
#       def __init__(self, length, width):
#             self.length = length
#             self.width = width
      
#       def area(self):
#             Area = self.length * self.width
#             print(f'Площадь прямоугольника равна: {Area}')
      
# instance = Rectangle(3, 5)
# instance.area()

############################################

# class Parent:
      
#       def __init__(self):
#             self.city = 'Erevan'
      
#       def country(self):
#             country = self.city
#             print(country)
            
# class Child(Parent):
      
#       def __init__(self):
#             self.city = 'Paris'
            
#       def country(self):
#             country = self.city
#             print(country)
            
# a = Parent()
# b = Child()

# a.country()
# b.country()

############################################

