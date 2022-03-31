# def calc(num1, num2, action):
#       if action == '+':
#             print('Результат:', num1 + num2)
#       elif action == '-':
#             print('Результат:', num1 - num2)
#       elif action == '/':
#             print('Результат:', num1 // num2)
#       elif action == '*':
#             print('Результат:', num1 * num2)

# calc(15, 12, '+')



# def max(number1, number2):
#       if number1 > number2:
#             print('Наибольшое число:', number1)
#       elif number1 == number2:
#             print('Числа равны.')
#       else:
#             print('Наибольшое число:', number2)
      
# max(15,22)



# def sum(mylist):
#       res = 0
#       for i in mylist:
#             res += i
#       print('Результат:', res)
      
      
# mylist = [15, 25, 40]
# sum(mylist)



# def multiply(mylist, multiplier):
#       res = []
#       for i in mylist:
#             i = i * multiplier
#             res.append(i)
#       print('Результат: ', end='')
#       for i in res:
#             print(i, end=' ')

# mylist = [10, 20, 30]            
# multiply(mylist, 2)



# def sum(string):
#       string = str(string)
#       nums = 0
#       letters = ''
#       for i in string:
#             if i.isdigit():
#                   nums += int(i)
#             else:
#                   letters += i
#       print('Сумма цифр в строке:', nums)
#       print('Сумма букв в строке', letters)
      
# sum('Hello140World1234')



# def  face_control():
#       ages = []
#       for i in range(0, 3):
#             age = input('Введите возраст: ')
#             ages.append(int(age))
#       for i in ages:
#             if i < 16:
#                   print('Неподходящий возраст!')
#                   break;
#       else:
#             print('Готовьтесь к отправлению!')

# face_control()