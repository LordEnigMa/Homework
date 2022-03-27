# students = {
#       'Std1' :  1,
#       'Std2' : 6,
#       'Std3' : 3,
#       'Std4' : 4,
#       'Std5' : 5,
#       'Std6' : 5,
#       'Std7' : 7,
#       'Std8' :4,
#       'Std9' : 9,
#       'Std10' : 2,
# }
# bad_students = {}
# good_students = {}
# res = 0

# for i in students.values():
#       res += i
# res /= len(students)
# print(res)

# for x, y in zip(students, students.values()):
#       if y > 4:
#             good_students.setdefault(x, y)
#       else:
#             bad_students.setdefault(x,y)
            
# for x, y in zip(good_students, good_students.values()):
#       print(str(x) + ': ' + str(y), end=', ')
# print()
# for x, y in zip(bad_students, bad_students.values()):
#       print(str(x) + ': ' + str(y),end=', ')

# name = input('Введите имя: ')
# for x, y in zip(students, students.values()):
#       if x == name:
#             print(x, y)



# Res = True
# mydict = {
#       'question1': {
#             'title': 'В какой из этих стран один из официальных языков - французский?',
#             'answers': {
#                   '1': 'Республика Гаити',
#                   '2': 'Кения',
#                   '3': 'Эквадор',
#                   '4': 'Венесуэла',
#             },
#             'ranswer': '1'
#       },
#       'question2': {
#             'title': 'В каком году произошла Куликовская битва?',
#             'answers': {
#                   '1': '1569',
#                   '2': '1380',
#                   '3': '1616',
#                   '4': '1773'
#             },
#             'ranswer': '2'
#       },
#       'question3': {
#             'title': 'Шкала Сковилла - это шкала оценки...',
#             'answers': {
#                   '1': 'Качества атмосферного воздуха',
#                   '2': 'Привлекательности женщин',
#                   '3': 'Остроты перца',
#                   '4': 'Уровня моря'
#             },
#             'ranswer': '3'
#       },
#       'question4': {
#             'title': 'Какой титул имел Дон Кихот?',
#             'answers': {
#                   '1': 'Барон',
#                   '2': 'Маркиз',
#                   '3': 'Идальго',
#                   '4': 'Вождь'
#             },
#             'ranswer': '3'
#       },
#       'question5': {
#             'title': 'Как называется самая глубокая точка поверхности Земли, находящаяся на дне Марианской впадины?',
#             'answers': {
#                   '1': 'Филиппинская плита',
#                   '2': 'Бездна Челленджера',
#                   '3': 'Кермадек',
#                   '4': 'Черное Логово'
#             },
#             'ranswer': '2'
#       }
# }

# while Res:
#       earnings = 0
#       for i in mydict:
#             print(mydict[i]['title'])
#             for x, y in zip (mydict[i]['answers'], mydict[i]['answers'].values()):
#                   print(x + '. ' + y)
#             answer = input('Выберите номер ответа: ')
#             if answer == mydict[i]['ranswer']:
#                   earnings += 500
#                   print('<==Ваш выигрыш:', str(earnings) + '$==>')
#             else:
#                   print('Вы проиграли!')
#                   Res = False
#                   break
#             if earnings == 1500:
#                   continue_answer = input('Ваш выигрыш составляет 1500$, вы хотите продолжить?(Да/Нет): ')
#                   if continue_answer == 'Нет':
#                         print('Игра окончена!')
#                         Res = False
#                         break



# word = 'exercises'
# mydict = {}

# for i in word:
#       if i not in mydict:
#             mydict.setdefault(i, word.count(i))
# print(mydict)



# a = 'a, 2, b, 5, c, 8, a, 4, e, 11'
# a = a.split(', ')
# mydict = {}
# char_list = []
# num_list = []
# new_num_list = []
# new_char_list = []

# for i in a:
#       if i.isdigit():
#             num_list.append(int(i))
#       else:
#             char_list.append(i)

# for i in char_list:
#       if i not in new_char_list:
#             new_char_list.append(i)
            
# for i in range(0, len(new_char_list)):
#       Sum = 0
#       indexs = []       
#       for u in range(0, len(char_list)):
#             if new_char_list[i] == char_list[u]:
#                   indexs.append(u)
      
#       for number in indexs:
#             Sum += num_list[number]
#       new_num_list.append(Sum)

# for x, y in zip(new_char_list, new_num_list):
#       mydict.setdefault(x,y)

# print(mydict)



# s="python"
# for i in range(0,len(s)+1):
#     print(s[:i])
# for i in range (len(s),0,-1):
#     print(s[:i-1])