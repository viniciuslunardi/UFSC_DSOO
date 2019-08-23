from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = Editora()
        self.__autor = Autor()
        self.__numero_capitulo = numeroCapitulo
        self.__titulo_capitulo = tituloCapitulo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
       return self.__titulo
    @property
    def ano(self):
        return self.__ano
    
    

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    ... Adicionar demais setters
    

    def incluirAutor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        ... Nao permitir insercao de Autores duplicados!

    def excluirAutor(self, autor: Autor):
        ...

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        ... Nao permitir insercao de Capitulos duplicados!

    def excluirCapitulo(self, tituloCapitulo: str):
        ...

    def findCapituloByTitulo(self, tituloCapitulo: str):
        ...

