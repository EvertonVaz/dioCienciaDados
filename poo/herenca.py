"""
Herença:
    Em programação herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

Benefícios da herença
    - Representa bem os relacionamentos do mundo real.
    - *Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
    - *É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.
"""

# Herença simples,
#         Veículo
#   ________|________      
#  |        |        |
# moto    carro   caminhão

class Veiculo():
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def __del__(self):
        print('metodo destrutor')
    
    def ligar_motor(self):
        print(f"{self.__class__.__name__} com o motor ligado\n", end='\n')

    def __str__(self) -> str:
        return f"{self.__class__.__name__} - {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas) -> None:
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self, carregado=False):
        print(f"{'Sim' if carregado else 'Não'} esta carregado")



moto1 = Moto('vermelha', '1234', 2)
print(moto1)
moto1.ligar_motor()


caminhao1 = Caminhao('azul', '4321', 8)
print(caminhao1)
caminhao1.esta_carregado()
caminhao1.esta_carregado(True)
caminhao1.ligar_motor()

carro1 = Carro('preto', '5678', 4)
print(carro1)
carro1.ligar_motor()



# Herença multipla
#                         animal
#                 __________|__________
#                |                     |
#             mamifero                ave
#      _________|______________________|
#     |         |       |              |
# cachorro    gato    leao        ornitorinco


class Animal():
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} - {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo
        

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass


class Ornitorrinco(Ave, Mamifero):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(cor_bico, **kwargs)
        print()
        print(Ornitorrinco.__mro__)


gato = Gato(nro_patas=4, cor_pelo='preto')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="marrom", cor_bico='preto')
print(ornitorrinco)
