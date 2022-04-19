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

# class Soda:
      
#       def __init__(self, additive):
#             self.additive = additive
            
#       def show_my_drink(self):
#             additive = self.additive
#             if additive == 0 or additive == '' or additive == '':
#                   print('Обычная газировка.')
#             else:
#                   print(f'Газировка и {additive}.')
                  
# instance = Soda(' ')
# instance.show_my_drink()

############################################

# class TriangleChecker:
      
#       def __init__(self, a, b, c):
#             self.a = a
#             self.b = b
#             self.c = c
      
#       def is_triangle(self):
#             a = str(self.a)
#             b = str(self.b)
#             c = str(self.c)
            
#             if a.isdigit() and b.isdigit() and c.isdigit():
#                   a = int(a)
#                   b = int(b)
#                   c = int(c)
#                   if a > 0 or b > 0 or c > 0:
#                         if a + b > c and a + c > b and b + c > a:
#                               print('Ура, можно построить треугольник!')
#                         else:
#                               print('Жаль, но из этого треугольник не сделать.')
#                   else:
#                         print('С отрицательными числами ничего не выйдет!')
#             else:
#                   print('Нужно вводить только числа!')
                  
# instance = TriangleChecker(4, 5, 10)
# instance.is_triangle()

############################################

# class KgToPounds:
      
#       def __init__(self, kg):
#             self.kg = kg
      
#       def set_kg(self, kg):
#             self.kg = kg
      
#       def get_kg(self):
#             print('Введённое количество кг:', self.kg)
            
#       def to_pounds(self):
#             kg = self.kg
#             pounds = int(kg * 2.2)
#             print(f'{kg} кг равно {pounds} фунтов.')
            
# instance = KgToPounds(100)
# instance.set_kg(120)
# instance.get_kg()
# instance.to_pounds()

############################################

# class Nikola:

#       def __init__(self, name):
#             self.fake_name = name
#             self.name = 'Николай'
            
#             if self.fake_name == self.name:
#                   print('Я Николай.')
#             else:
#                   print(f'Я не {self.fake_name}, а {self.name}.')
                  
# instance = Nikola('Николай')