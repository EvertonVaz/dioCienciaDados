class Bicicleta:
    # metodo construtor da classe
    """
        O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__.
    """
    def __init__(self, cor, modelo, ano, valor):
        print("inicializando o objeto")
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # metodo destrutor da classe
        """
            O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários quanto em C++ porque o Pyton tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__.
        """
    def __del__(self):
        print('destruindo o objeto')
        
    # metodos ou comportamentos da classe
    def buzinar(self):
        print('primm primm')

    def correr(self):
        print('vrrruuuummm')
    
    def parar(self):
        print('parando bicicleta')
        print('bicicleta parada')

    """def __str__(self) -> str:
        return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'"""
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}:\n\t{', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
        


# instanciando o objeto
bike1 = Bicicleta('preta', 'caloi', 2022, 1000)


#utilizando seus metodos
bike1.correr()
bike1.buzinar()
bike1.parar()
print(bike1)