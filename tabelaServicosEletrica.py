#usar case switch ~ Dicionarios para selecao das opcoes
ServicosEletrica = dict([('0','Hl Soluções Elétricas'),('1','Eco'),('2','D.A.S. Serviços E Manutencao'),
('3','Ética Imóveis'),('4','A.M Instalações Elétricas'),('5','Luiz Carlos Eletricista'),
('6','Instalação Elétrica E Manutenção Geral'),('7','Electrolux,Brastemp E Cônsul Grupo Rs'),
('8','Manutenção Elétrica, Painéis E Outros Serviços'),('9','Ibf Construção E Manutenção Predial')])

P = input("Digite um num entre 0 e 9: ")
print("Voce contratou:", ServicosEletrica[P])

print("Deseja encerar operaçao?: ")
R = input()
if (R == 'sim'):
    print("A empresa contatada logo entrara em contato. Tenha um bom dia.")
    pass
else:
    print("Por favor, selecione mais de um servico.")
    pass