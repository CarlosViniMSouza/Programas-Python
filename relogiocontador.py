##Relogio em python##

x = input()

HH = int(x[0]+x[1])

MM = int(x[3]+x[4])

SS = int(x[6]+x[7])

y = input()

hh = int(y[0]+y[1])

mm = int(y[3]+y[4])

ss = int(y[6]+y[7])

y1 = (HH*3600)+(MM*60)+SS
y2 = (hh*3600)+(mm*60)+ss
y3 = y2-y1

##Bloco matematico##
if (y3 < 0):

	a = 86400 - y1

	a2 = a + y2

	Ht = a2//3600

	a = a2 % 3600

	Mt = a//60

	St = a % 60

else:

	Ht = y3//3600

	z = y3 % 3600

	Mt = z//60

	St = y3 % 60

if(Ht < 10):

	h = '0'+ str(Ht)

	Ht = h
if(Mt < 10):

	m = '0'+ str(Mt)

	Mt = m
if(St < 10):

	s = '0'+ str(St)

	St = s
print(str(Ht)+":"+str(Mt)+":"+str(St))