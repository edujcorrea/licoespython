if __name__ == "__main__":
	print('arquivo1 está sendo executado diretamente')
	print('A variável __name__ é nesse caso: ' + __name__)
else:
	print('arquivo1 está sendo importado')
	print('A variável __name__ é nesse caso: ' + __name__)