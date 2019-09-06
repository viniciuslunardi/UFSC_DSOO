from abc import ABC, abstractmethod
class Animal(ABC):
	@abstractmethod
	def __init__(self, tamanho_passo: int):
		self.__tamanho_passo = tamanho_passo

	@property
	def tamanho_passo(self):
		return self.__tamanho_passo

	@tamanho_passo.setter
	def tamanho_passo(self, tamanho_passo):
		self.__tamanho_passo = tamanho_passo

	@abstractmethod
	def mover(self):
		return "O animal deslocou {self.__tamanho_passo} passos."
	
	@abstractmethod
	def produzirSom(self):
		return "Barulho de animal"
