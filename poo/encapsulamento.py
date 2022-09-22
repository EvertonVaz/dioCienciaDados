"""
Proteção de acesso
    O encapsulamento é um dos conceitos fundamentais em programação orientada a objetos. Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

    modificadores de acesso em python é feito por convenção, alterando o nome do recurso para definir se a variável é pública ou privada.
    - Público: Pode ser acessado de fora da classe. ( exemplo )
    - Privado: Só pode ser acessado pela classe.    ( _exemplo )
 
"""

class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo #convenção para recursos privados

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
