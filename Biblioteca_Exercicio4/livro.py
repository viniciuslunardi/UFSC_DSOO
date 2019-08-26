from editora import Editora
from autor import Autor
from capitulo import Capitulo
class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = Editora(codigo, nome)
        self.__autor = Autor(codigo, nome)
        self.__numero_capitulo = numeroCapitulo
        self.__titulo_capitulo = tituloCapitulo
        self.capitulos = []
        self.autores = []

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
        return self.__autor

    @property
    def numero_capitulo(self):
        return self.__numero_capitulo

    @property
    def titulo_capitulo(self):
        return self.__titulo_capitulo
    
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

    @numero_capitulo.setter
    def numero_capitulo(self, nc):
        self.__numero_capitulo = nc

    @titulo_capitulo.setter
    def titulo_capitulo(self, tc):
        self.__titulo_capitulo = tc

    def incluirAutor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        self.autores.append(autor)

    def excluirAutor(self, autor: Autor):
        pass

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        #Nao permitir insercao de Capitulos duplicados!
        pass
    
    def excluirCapitulo(self, tituloCapitulo: str):
        pass

    def findCapituloByTitulo(self, tituloCapitulo: str):
        pass

