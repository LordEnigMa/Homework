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

# def calc():
#       action = ''
#       nums = []
      
#       try:
#             string = input('Введите действие: ')
#             if ' ' in string:
#                   print('Напишите без пробелов.')
#                   calc()
#             if ',' in string:
#                   print('Нецелые числа писать через точку.')
#                   calc()
#             if len(string) <= 2:
#                   calc()
#             for i in range(1, len(string)):
#                   if string[i] == '.':
#                         continue
#                   if string[i].isdigit():
#                         continue
#                   else:
#                         nums.append(float(string[:i]))
#                         action = string[i]
#                         nums.append(float(string[i+1:]))
#                         break
#             if len(nums) < 2:
#                   calc()
#       except:
#             calc()
      
#       if action == '+':
#             print('Результат: ', nums[0] + nums[1])
#       elif action == '-':
#             print('Результат: ', nums[0] - nums[1])
#       elif action == '*':
#             print('Результат: ', nums[0] * nums[1])
#       elif action == '/':
#             if nums[1] == 0:
#                   calc()
#             else:
#                   print('Результат: ', nums[0] / nums[1])
#       else:
#             calc()
                  
# calc()