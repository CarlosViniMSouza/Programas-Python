#iniciando a aula:

adm = False #Boolean -> Booleano -> Bool
print(adm)

 #Comparation - Igual

comp_igual = 1 != 1
print(comp_igual)

#Sequences of prints:
print(2!=2) #False
print(1>=0) #True
print(5<=5) #True

#Atv:
print(98 != -98 & 15<=-15) #?
print(2>=-2) #True
print(2<=-2) #False

print(not (False and True))
print(not False and True)
#see with a '()' changed the result.

print(not (not (True))) #True
print(not True != (not False) or True == False) #True
print(True == False and True) #False

print(False != (True or False)) #True
print(False != (True & False)) #False

print(not (not (True))) #True
print(not True != (not False) or True==False) #True
print(True != False or False) #True

# ordem de resolução : not -> and -> or

#If, else and elif:
adm = 0
if adm == False:
    print("Access Completed")
#pq a saída é "Access Completed"?