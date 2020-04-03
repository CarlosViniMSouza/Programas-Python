import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=15, width=200)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Prosseguindo...
('Aula 3 - Introdução a listas')
('>>>a = [1,'hello',2]')
('>>>type(a)')
('<class list>')
('Listas são junçoes de inumeros tipos de dados (int, bool, str, float)')

("print('Comando for e range')
("print('Sintaxe: for (variavel) in lista:')
("print('usamos para imprimir numeros em listas')

("print('Ex.: nesse caso ele imprime o num escrito 8 vezes')
("a = int(input('digite numero: '))

("print('Ex2.: nesse caso ele imprime de 2 até 29 se o numero digitado estiver no int(2-29)')
("a = int(input('digite4.5: ')
("for i in range(2,30): ')
("   print(a)')

("print('Ex3.: a lista vai de 100 até 2210, pulando de 100 em 100 numeros')
("b = int(input('digite5: '))
("for i in range(100,2201,100):')

("print('VOLTANDO AO FOR')\
("print('Ex4.: começa no 2 e termina no a+1')
("c = int(input('digite6: '))
("for i in range(2,c):')

("print('Variável Acumuladora (A)')
("print('aqui voce decide a quantia de numeros que serao somados')
("print('e os proprios numeros a serem somados')

("print('Ex5.: Somatorio a ser definido  pelo usuario')
("d = int(input('digite7: '))

("for i in range(d):')
("    B = int(input('digite7.1: '))
("    A = A + B
("print(str(A))
('Ex6.: Calculando potencias de base 2')
('a = int(input(digite8: ))')
('i = 1000')
('A = 1 #correspondendo a 2^0...#')
('while i<=a:')
('print('2^'+str(i)+'='+str(A))')
('i = i+1')
('A = A*2')
(' 'a' é a quantia potenciações a calcular.')
('OBS.: Não executaremos o programa acima pois ele ficará eternamente calculando')

("print('Ex7.:Calculando raizes')
("a = int(input('digite9: '))
("A = a")
("for A in range(1,a):")
("    A = A*(0.5)\n")
("print('Raizes: '+str(A))")
("print('a variavel armazenadora dará a raiz, quantas vezes queira")

("print('##Comando break')
("print('termina a execução de uma laço')
("print('Ex8.: Fazendo um laço ate 'a' ser maior que 'í')
("a = int(input('digite10: '))
("i = input()')
("for i in range (1,101):")
("    if (i>a):")
("        break")
("    print(i)")
("print('fim do laço')")

('##Comando continue')\n")
('faz a execução de 1 laço ir p/ final.')\n")
('Ex9.: Fazendo mais um laço")

("i = 20")
("while a<=10:")
("    if (i==5):")
("        continue")
("    print(i)\)
("    i = i+1\)
("print('fim do laço...")
("##fim da aula 03##")
"""
T.insert(tk.END, quote)
tk.mainloop()
