import json

# mydict = {
#       'First Name': 'Eduard',
#       'Last Name': 'Minasyan',
#       'Age': 18,
#       'Country': 'Armenia',
#       'City': 'Yerevan'
# }

file_name = 'data.json'

###################################################

# with open(file_name, 'w') as  file:
#       json.dump(mydict, file)

###################################################

# file = open(file_name)
# json_data = json.load(file)

# for x, y in zip(json_data, json_data.values()):
#       print(str(x) + ': ' + str(y))
      
###################################################

# file = open(file_name)
# json_data = json.load(file)

# search = input('Введите слово: ')

# if search in json_data:
#       print('Такое слово есть в файле.')
# elif search in json_data.values():
#       print('Такое слово есть в файле.')
# else:
#       print('Такого слово нету в файле.')

###################################################

# first = ['Ani', 'Jessy', 'Ben']  
# second = [1, 2, 3]
# mydict = {}

# for x, y in zip(second, first):
#       mydict.setdefault(x, y)
      
# with open('mydict.txt', 'w') as file:
#       file.write(str(mydict))

###################################################

# lyrics = '''Here's to the ones that we got
# Cheers to the wish you were here, but you're not
# 'Cause the drinks bring back all the memories
# Of everything we've been through
# Toast to the ones here today
# Toast to the ones that we lost on the wayn
# 'Cause the drinks bring back all the memories
# And the memories bring back, memories bring back you'''

# with open('lyrics.json', 'w') as file:
#       json.dump(lyrics, file)

###################################################

# def multples_sum(number):
#       Sum = 0
      
#       for i in range(0, number):
#             if i % 3 == 0 or i % 5 == 0:
#                   Sum += i
      
#       return Sum

# with open('multiples_sum.json', 'w') as file:
#       json.dump(multples_sum(10), file)

###################################################

# count = 0
# char_list = ['a', 'e', 'i', 'o', 'u', 'y']
# string = input('Введите слово: ').lower()

# for i in string:
#       if i in char_list:
#             count += 1
            
# with open('vowels_count.json', 'w') as file:
#       json.dump(count, file)

###################################################

# file = open('text.txt')
# mylist = file.read().split(' ')
# mydict = {}

# for i in mylist:
#       mydict.setdefault(i, mylist.count(i))
      
# print(mydict)

###################################################

my_list = ['a', 'b', 'a', 'c', 'b']

def no_repeat(mylist):
      new_list = []
      for i in mylist:
            if i not in new_list:
                  new_list.append(i)

      return new_list

print(no_repeat(my_list))