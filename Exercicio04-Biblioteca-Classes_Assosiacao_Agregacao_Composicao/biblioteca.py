from livro import Livro
class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if (livro is not None) and (isinstance(livro, Livro)):
            if not self.__livros.count(livro):
                self.__livros.append(livro)

    def excluirLivro(self, livro: Livro):
        if (livro is not None) and (isinstance(livro, Livro)):
            if self.__livros.count(livro):
                self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
