#study methods for strings and functions!

user_n1 = ['name', 'year', 'c.e.p', 17, 34.5]

user_n2 = ('music', 'artist', 'movie', 16, 32.6)

user_n3 = {'answer1' : 'resp1',
           'answer2' : 'resp2',
           'answer3' : 'resp3',
           'number1' : 15,
           'number2' : 30.3}

#datas created, testing methods!

user_n1.append(25.75) #add the number in the end of list.
user_n2.count('music') #unknow
user_n3 = user_n3.fromkeys(user_n3, 'Empty') #replace values by 'Empty'

#printing results after test's
print(user_n1)
print(user_n2)
print(user_n3)