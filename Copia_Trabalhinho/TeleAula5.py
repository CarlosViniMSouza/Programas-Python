import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=15, width=200)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Prosseguindo...
"('Aula 05 - strings')\n").pack_configure()
"('são listas imutaveis de caracteres entre aspas')\n")
"('exemplo de str.: a = 'abcdef' ')\n").
"('veremos alguns comandos para você treinar')\n")
"('OBS.: AQUI É APENAS TEXTOS, SEM PROGRAMAS EXEMPLO')\n")

"('para cortar o comando e botar na próxima linha = (\ n)')\n")
"('aa = abc\ ndef ')\n")
"('print(aa)')\n")
"('abc')\n")
"('def')\n")

"('para somar string e reptir as listas = (+ e *)')\n")
"('>>>valeu+falou')\n")
"('valeufalou')\n")
"('>>>3*xyz')\n")
"('xyzxyz')\n")

"('devolve parte da string = (slice)')\n")
"('>>>a = beijo')\n")
"('>>>a = [1:4]')\n")
"('eo')\n")
"('string vazia = ("") ')\n")
"('NOTA = teste os comandos depois')\n")

"##funções\n")
"('elementos strings podem ser percorridos por laço for')\n")
"('Ex.: leia uma string e imprima sua inversa desse jeito:')\n")
"(' st = input(digite: )')\n")
"('inv = (" ")')\n")
"('for x in st')\n")
"('    inv = x + inv')\n")
"('print(inv)')\n")

"#mais comandos...\n")
"('O strip retorna a string original')\n")
"('>>>x = \ n abcdef \ n')\n")
"('>>>x')\n")
"('\ n abcdef \ n')\n")
"('print(x)')\n")
"('abcndef')\n")
"('x.strip()')\n")
"('abcndef')\n")

"('O operador in verifica se uma substring está contida na string')\n")
"('>>>'tho' in 'python' ')\n")
"('True')\n")
"('>>>'tring' in 'python' ')\n")
"('False')\n")

"('O método 'find' diz onde localiza-se uma substring')\n")
"('>>>p = 'python' ')\n")
"('>>>p.find('tho') ')\n")
"('2')\n")

"('O método 'split(sep)' separa string usando sep como separador')\n")
"('a = '1,2,3' ')\n")
"('a.split(':') ')\n")
"('['1','2','3']')\n")

"('O método 'split()' usa \ n e sep')\n")
"('>>>b = 'Tratamos disso ontem' ')\n")
"('>>>b.split() ')\n")
"('['Tratamos'','disso'','ontem']')\n")
"('teste as operações depois')\n")

"('Operações,funções e métodos')\n")
"('Método 'replace' troca as ocorrencias de uma substring por outra na string.')\n")
"('Método 'list' torna string em lista de caracteres')\n")
"(Método 'join' recebe como lista e retorna uma string concatenada)\n")
"(teste as funcionalidades)\n")

"##fim da Aula 5 STRINGS\n").
"""
T.insert(tk.END, quote)
tk.mainloop()
