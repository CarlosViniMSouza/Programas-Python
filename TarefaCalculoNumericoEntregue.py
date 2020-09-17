import numpy as np

print("Resolveremos os problemas pela ordem:")
#declaramos as matrizes 'A', 'B' e 'C' das matrizes em questão da seguinte forma:
#An = np.array([[],[]]))
#Bn = np.array([[],[]]))
#Cn = np.linalg.solve(An,Bn)
#print(Cn)

#print("Proxima Questao\n")
#Para obtermos a inversa da matriz
#NomeMatriz = np.array([[],[],[]])
#NomeMatriz_inversa = np.linalg.inv(NomeMatriz)
#NomeMatriz_inversa
print("Vamos Começar:\n\n")

print("#Exemplo 4.1.1")
A1 = np.array([[1,1,1],[4,4,2],[2,1,-1]])
B1 = np.array([[1],[2],[0]])
C1 = np.linalg.solve(A1,B1)
print(C1)
print("Vejamos outro exemplo;\n\n")

print("#Exemplo 4.1.3")
A2 = np.array([[1,1,1],[2,1,-1],[2,2,1]])
B2 = np.array([[1],[0],[1]])
C2 = np.linalg.solve(A2,B2)
print(C2)
print("Vejamos outro exemplo;\n\n")

print("#E 4.1.3")
A = np.array([[1,2,-1],[1,2,0],[2,1,-1]])
A_inversa = np.linalg.inv(A)
print(A_inversa)
print("Vejamos outro exemplo;\n\n")

print("#E 4.1.4")
print("D = np.array([[],[]])")
print("D_inversa = np.linalg.inv(D)")
print("D_inversa\n\n")

#D^-1 = 1/(ad - bc)*D_inversa #quando a matriz é inversivel  assim tambem...

print("#Ex 4.1.1")
A3 = np.array([[1,1,1],[1,0,10],[1,10,1]])
B3 = np.array([[0],[-48],[25]])
C3 = np.linalg.solve(A3,B3)
print(C3)

print("#Ex 4.1.2")
A4 = np.array([[1,1,1],[1,0,10],[0,10,1]])
B4 = np.array([[0],[-48],[25]])
C4 = np.linalg.solve(A4,B4)
print(C4)

print("\nAqui veremos a lista resolvida questao por questao;\n")

print("Q.1\n")
#A11 = np.array([[3,-2,5,1],[-6,4,-8,1],[9,-6,19,1],[6,-4,-6,15]])
#B11 = np.array([[7],[-9],[23],[11]])
#C11 = np.linalg.solve(A11,B11)
#print(C11)

print("Q.2\n")
A12 = np.array([[2,2,1,1],[1,-1,2,-1],[3,2,-3,-2],[4,3,2,1]])
B12 = np.array([[7],[1],[4],[12]])
C12 = np.linalg.solve(A12,B12)
print(C12)

##a questao abaixo tem ocasionados problemas de execução

#print("Q.3 ~ letra(a) \n")X = input(float("digite a variável n1: ")
#Y = input(float("digite a variavel n2: ")
#Z = input(float("digite a variavel n3: ")
#A13 = np.array([[1.0,1.0,1.0],[1.0,1.0,1.0],[0.0,1.0,1.0]])
#B13 = np.array([[X],[Y],[Z]])
#C13 = np.linalg.solve(A13,B13)

print("Q.3 ~ letra(b) \n")
A13 = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
B13 = np.array([[1],[0],[0]])
C13 = np.linalg.solve(A13,B13)

print("Q.4\n")
print("Letra(a)~A questao trata de matematica pura, o que impede a efetividade da criacao de um programa para tal problema;")
print("Letra(b)~O programa abaixo calculara o det da matriz C12 e C13\n")
C12 = np.linalg.solve(A12,B12)
detC12 = A[0,0]*A[1,1]-A[0,1]*A[1,0]
print(detC12)
A13 = (np.array([[2,-1,0],[-1,2,-1],[0,-1,2]]))
detC13 = A[0,0]*A[1,1]-A[0,1]*A[1,0]
print(detC13)

#print("Q.5\n")
#print("Letra(a)~Temos:\n")
#float(a) = 0.004
#float(b) = 15.73
#float(c) = 0.423
#float(d) = -24.72
#A matriz que iremos fazer é:
#A14 = np.array([[4/1000,1573/100],[423/1000,-2472/100]]))
#B14 = np.array([[15.77],[-20.49]]))
#C14 = np.linalg.solve(A14,B14)
#print("%.4f"%C14) 

#print("Letra(b) ~ Vejamos:\n")
#A14 = np.array([[2,2],[2,2]])
#B14 = np.array([[5],[6]])
#C14 = np.linalg.solve(A14,B14)

print("Q.6~Mostre que nao tem solucao o sistema abaixo:\n")

A15 = np.array([[1,2,1],[2,3,1],[3,5,2]])
B15 = np.array([[3],[5],[1]])
C15 = np.linalg.solve(A15,B15)
print(C15)

print("Q.7~Resolva os sistemas:\n")

print("Letra(a)~Resolvendo:")
A16 = np.array([[16,5],[3,2.5]])
B16 = np.array([[21],[5.5]])
C16 = np.linalg.solve(A16,B16)
print(C16)

print("Letra (b)~Iteracao por ser parte integrante da matematica pura, nao faremos o programa\n")

print("Q.8\n")
print("Como a resolucao trata-se de matematica pura, não sera possivel a efetivação do programa solicitado.\n")

print("Q.9\n")
A17 = np.array([[1,-2,7,2],[2,5,-3,1],[9,-6,4,1],[4,-3,-6,7]])
B17 = np.array([[-18],[31],[35],[15]])
C17 = np.linalg.solve(A17,B17)
print(C17)

print("Q.10\n")
print("#Como a resolucao trata-se de matematica pura,\n não sera possivel a efetivação do programa solicitado.")

print("Q.11\n")
print("#Encontre a decomposição LU das matrizes")

#(a)
A5 = np.array([[16,5],[1,2]])
B5 = np.array([[1],[1]])
C5 = np.linalg.solve(A5,B5)
print(C5)

#(b)
A6 = np.array([[5,2,1],[3,1,4],[1,1,3]])
B6 = np.array([[1],[1],[1]])
C6 = np.linalg.solve(A6,B6)
print(C6)

#(c)
A7 = np.array([[2,1,0],[1,6,4],[0,4,11]])
B7 = np.array([[1],[1],[1]])
C7 = np.linalg.solve(A7,B7)
print(C7)

#(d)
A8 = np.array([[1,2],[3,4]])
B8 = np.array([[1],[1]])
C8 = np.linalg.solve(A8,B8)
print(C8)

print("Q.12\n")

print("por ser uma questao de matematica pura, nao sera possivel a efeitivacao de um programa para resolucao do problema\n")

print("Q.13\n")

print("por ser uma questao de matematica pura, nao sera possivel a efeitivacao de um programa para resolucao do problema")

print("Q.14\n")

A5_inversa = np.invert(A5)
A6_inversa = np.invert(A6)
A7_inversa = np.invert(A7)
A8_inversa = np.invert(A8)
print(A5_inversa)
print("\n")
print(A6_inversa)
print("\n")
print(A7_inversa)
print("\n")
print(A8_inversa)
print("\n")
print("Lista encerrada.")