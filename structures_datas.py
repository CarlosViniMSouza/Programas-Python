# started in : 08:14 - 27/08/2020

# structures types : lists, tuples, dictionaries and sets.
tuple_n1 = (0, 1, 2, "Dev", "Anony", "Bra") # item 1 (flexible and mutable)

list_n1 = [0, 1, 2, "Dev", "Anony", "Bra"] # item 2 (inflexible and inmutable)

sets_n1 = {0, 1, 2, "Dev", "Anony", "Bra"} # item 3 (inflexible and mutable)

dict_n1 = { 'name' : 'DeveloperAnonymous',
            'age' : 19,
            'country' : 'Brazil' } # item 4 (flexible and mutable)

# coding and testing structures :
dict_n2 = {} # Let's complete it :

dict_n2['name'] = input('your name please:')
dict_n2['age'] = input('your age also:')
dict_n2['adress'] = input('lastly, your adress:')

for values in dict_n2.values():
    print(values)

#how to start a structure without values:
# list = []
# tuple = ()
# dict = {}
# set = set()