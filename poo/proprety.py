"""
Propreties
    Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.
"""
from datetime import date

class Foo:
    def __init__(self, x=None) -> None:
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x -= 1


foo = Foo(1)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

class Pessoa:
    def __init__(self, nome, ano_nascimento) -> None:
        self._ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = date.today().year
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa('everton', 1988)

print(f'Nome: {pessoa.nome.title()} | Idade: {pessoa.idade}')