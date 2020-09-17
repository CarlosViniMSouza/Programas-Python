user_n1 = ['name', 'year', 'c.e.p', 17, 34.5]
user_n3 = {'answer1' : 'resp1',
           'answer2' : 'resp2',
           'answer3' : 'resp3',
           'number1' : 15,
           'number2' : 30.3}

user_n1.append(25.75) #add the number in the end of list.
user_n3 = user_n3.fromkeys(user_n3, 'Empty') #replace values by 'Empty'

print(user_n1)
print(user_n3)

#*Which is output?*#