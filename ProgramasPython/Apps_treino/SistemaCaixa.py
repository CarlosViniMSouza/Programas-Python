#caixamercado em python com classes
def cliente():
    nome = input("Insira seu nome por favor: ")
    num_conta = input("Insira sua conta: ")
    saldo = input("Insira seu saldo com loja, por favor: ")
    print("\n")
    pass

def produto(prod1, prod2, prod3):
    print("\nA seguir, coloque o nome dos produtos\n")
    prod1 = input("quem é o p1?: ")
    prod2 = input("quem é o p2?: ")
    prod3 = input("quem é o p3?: ")
    print("\n")
    pass

def quantia(self, qu1, qu2, qu3):
    print("\nA seguir, coloque a quantia de cada produto\n")
    self.qu1 = int(input("digite a quantia de q1: "))
    self.qu2 = int(input("digite a quantia de q2: "))
    self.qu3 = int(input("digite a quantia de q3: "))
    print("\n")
    pass
    
def preco(self, preco1, preco2, preco3):
    print("\nA seguir, coloque o preco de cada produto\n")
    self.preco1 = float(input("Digite o preco do prod1: "))
    self.preco2 = float(input("Digite o preco do prod1: "))
    self.preco3 = float(input("Digite o preco do prod1: "))
    pass 

def custo(self, cus1, cus2, cus3):
    self.cus1 = self.qu1 * self.preco1 
    self.cus2 = self.qu2 * self.preco2 
    self.cus3 = self.qu3 * self.preco3
    print("\n")
    pass
    
    A = cliente()
    B = produto()
    C = quantia()
    D = custo()
    print(A)
    print(B)
    print(C)
    print(D)