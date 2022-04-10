# i = 1
# while True:
#       if i % 12 == 0 and i % 15 == 0:
#             print(i)
#             break
#       else:
#             i += 1



# even_counter = 0
# odd_counter = 0

# for i in range(1, 100):
#       if i % 2 == 0:
#             even_counter += 1
#       else:
#             odd_counter += 1
            
# print(even_counter, odd_counter)



# n1 = 0
# n2 = 1
# fib_sum = 1

# print(0)
# while True:
#       print(fib_sum)
#       if fib_sum < 40:
#            fib_sum = n1 + n2
#            n1 = n2
#            n2 = fib_sum
#       else:
#             break



# string = 'python 3.9'
# res = 0

# for i in string:
#       if i.isdigit():
#             res += int(i)

# print(res)



# number = 73421
# res = 0

# for i in str(number):
#     res += int(i)
    
# print(res)


# def fact():
#       n = int(input('Write number: '))
#       res = 1

#       for i in range(1, n + 1):
#             res *= i
            
#       print(res)



# age = int(input('Write age: '))
# male = input('Write male: ')

# if age >= 18 and age <= 20:
#       if male.lower() == 'male':
#             print('You are male!')
#       elif male.lower() == 'female':
#             print('You are female!')
#       else:
#             print('We don`t know who you are.')
# else:
#       print('Your age is not suitable.')
      


# list = [ 0,1,5,6,13,29,33,24,28]

# for i in list:
#       if i % 2 == 0:
#             print(i)



# for i in range(1, 50):
#       if i % 3 == 0:
#             print(i)



# res = 0

# for i in range(1, 100):
#       if i % 5 == 0:
#             res += i
#             print(res)
            
# print(res)



# from math import gcd # Функция, которая считает наибольшой общий делитель
# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))

# while num_1 != num_2:
#       if num_1 > num_2:
#             num_1 = num_1 - num_2
#       else:
#             num_2 = num_2 - num_1

# print(num_1)