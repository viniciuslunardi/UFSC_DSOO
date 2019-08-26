from editora import Editora
from autor import Autor
from capitulo import Capitulo
class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__capitulos = []
        self.__autores = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autor(self):
        for i in range(len(self.__autores)):
            return self.__autores

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @editora.setter
    def editora(self, cod, nome):
        self.__editora = Editora(cod, nome)

    def incluirAutor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        autor_len = len(self.__autores + 1)
        self.__autores.append(autor, autor_len)

    def excluirAutor(self, autor: Autor):
        self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        #Nao permitir insercao de Capitulos duplicados!
        if self.__capitulos != numeroCapitulo:
            pass
    
    def excluirCapitulo(self, tituloCapitulo: str):
        pass

    def findCapituloByTitulo(self, tituloCapitulo: str):
        pass


