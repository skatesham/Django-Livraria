from django.db import models

class Autor(models.Model):
	nome = models.CharField(max_length=255)
	idade = models.IntegerField();
	
	def __str__(self):
		return self.nome

class Editora(models.Model):
	nome = models.CharField(max_length=255)
	avaliacao = models.IntegerField()
	
	def __str__(self):
		return self.nome

class Livro(models.Model):
	nome = models.CharField(max_length=255)
	paginas = models.IntegerField(default = 100)
	preco = models.DecimalField(max_digits=10, decimal_places=2)
	avaliacao = models.FloatField()
	autores = models.ManyToManyField(Autor)
	editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
	data_pub = models.DateField()
	
	def __str__(self):
		return self.nome

class Loja(models.Model):
	nome = models.CharField(max_length=255)
	livros = models.ManyToManyField(Livro)
	quantidade_de_clientes = models.PositiveIntegerField()
	
	def __str__(self):
		return self.nome

