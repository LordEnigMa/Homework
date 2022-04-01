# def generator():
#       symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '/', '\\', '\'', '\"', '`', '~', '<', '>', '.', ',', ':', ';', '?']
#       char_count = 0
#       nums_count = 0
#       password = input('Enter password: ')

#       try:
#             if len(password) > 7:
#                   if ' ' in password:
#                         print('Нельзя писать пробел!')
#                         generator()
#                   for item in password:
#                         if item.isdigit():
#                               nums_count += 1
#                         if item in symbols:
#                               char_count += 1
#                   if nums_count > 1 and char_count > 1:
#                         print('Надёжный пароль!')
#                   else:
#                         print('Повторите попытку!')
#                         generator()
#             else:
#                   print('Повторите попытку!')
#                   generator()
#       except KeyboardInterrupt():
#             pass

# generator()

#####################################################

def calc():
      action = ['+', '-', '/', '*']
      nums = []
      
      try:
            string = input('Введите действие: ')
            if ' ' in string:
                  print('Напишите без пробелов')
            for i in range(1, len(string)):
                  if i in string: 
                        nums = string.split(i)
                  else:
                        calc()
                  if i == '+':
                        print('Результат: ', sum(nums))
                        break
                  if i == '-':
                        print('Результат: ', nums[0] - nums[1])
                        break
                  if i == '*':
                        break
                        print('Результат: ', nums[0] * nums[1])
                  if i == '/':
                        try:
                              x = nums[0] / nums[1]
                              print('Результат: gadgad', x)
                              break
                        except:
                              calc()
      except:
            calc()

calc()