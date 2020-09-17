#creating analysis basic
#detC(n) = A[0,0]*A[1,1]-A[0,1]*A[1,0]
#cubo(n) = (c[0, c[1], c[2], c[3]])
#cubo(n) = (receita, ganhos, lucros, reservas)
#testing in ready...
import numpy as np
import matplot as mt

def setor1():
    cubo01 =  np.array([[], [], [], []])
    cubo02 =  np.array([[], [], [], []])
    cubo03 =  np.array([[], [], [], []])
    cubo04 =  np.array([[], [], [], []])
    cubost1 = np.linalg.solve(cubo01 ,cubo02, cubo03, cubo04)
    pass

def setor2():
    cubo05 =  np.array([[], [], [], []])
    cubo06 =  np.array([[], [], [], []])
    cubo07 =  np.array([[], [], [], []])
    cubo08 =  np.array([[], [], [], []])
    cubost2 = np.linalg.solve(cubo05 ,cubo06, cubo07, cubo08)
    pass

def setor3():
    cubo09 =  np.array([[], [], [], []])
    cubo10 =  np.array([[], [], [], []])
    cubo11 =  np.array([[], [], [], []])
    cubo12 =  np.array([[], [], [], []])
    cubost3 = np.linalg.solve(cubo09 ,cubo10, cubo11, cubo12)
    pass

Analise1 = setor1()
An01 = input("insira valores cubo01: ")
An02 = input("insira valores cubo02: ")
An03 = input("insira valores cubo03: ")
An04 = input("insira valores cubo04: ")
##insirindo informacoes do cubo 1 de informacoes

Analise2 = setor2()
An02 = input("insira valores cubo05: ")
An02 = input("insira valores cubo06: ")
An03 = input("insira valores cubo07: ")
An04 = input("insira valores cubo08: ")
##insirindo informacoes do cubo 2 de informacoes

Analise3 = setor3()
An03 = input("insira valores cubo09: ")
An02 = input("insira valores cubo10: ")
An03 = input("insira valores cubo11: ")
An04 = input("insira valores cubo12: ")
##insirindo informacoes do cubo 3 de informacoes

def Det(self, C1, C2, C3):
    self.C1 = self.cubost1
    self.C2 = self.cubost2
    self.C3 = self.cubost3
    self.C4 = (self.cubost1+self.cubost2+self.cubost3)/3
    
    if (self.C4 <= 0):
        {
            print("Analise concluida com sucesso")
        }
        pass
    else:
        print("ERRO")
        pass

#    "python.pythonPath": "C:\\Users\\user\\Anaconda3-2019.10",