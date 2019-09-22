"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array = array
        self.arrayOrdenado = []

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        for i in range(self.array):
            if self.array[i] < self.array[i-1]:
                self.arrayOrdenado.append(i)                        
        return self.arrayOrdenado
    def toString(self):
        for i in self.array:   
            return print(str(i))

ar = [1,4,6,2,3,8]
ord = Ordenacao(ar)
ord.ordena()