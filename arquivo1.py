"""
Este módulo de exemplo mostra vários tipos de documentação disponíveis para uso com pydoc. Para gerar documentação HTML para este módulo, comando:

pydoc -w foo

"""

class Pessoa(object):
	"""
	encapsula um nome e uma idade.
	"""
	def __init__(self, nome, idade):
		"""
		Construa um novo objeto 'Pessoa (Person)'
		
		:parâmetro name: O nome da pessoa
		:parâmetro age: A idade da pessoa
		:return: não retorna nada
		"""
		self.nome = nome
		self.idade = idade

def ImprimeSaudacao(saudacao):
	"""
	Imprime saudacao no visor.
	"""
	print(saudacao)

if __name__ == '__main__':
	p = Pessoa('Fulano de Tal', 70)
	ImprimeSaudacao("Olá, seja bem vindo!")