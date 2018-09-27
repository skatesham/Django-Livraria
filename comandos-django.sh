Comandos

>> Ambiente Virtual <<

	$ sudo apt-get install python3-venv

	$ python3 -m venv ~/Python\ Venv/dj-21

	$ pip freeze

	$ source activate

>> Django startproject

	$django-admin startproject livraria

	$python3 maneger.py startapp estoque

	> APP é um módulo python que pode ser usado para um programa


	> O Servidor Django interage com o usuário por Request and Responses

>> CONFIGURANDO BANCO DE DADOS

	$ python3 manage.py makemigrations

	$ python3 manage.py migrate

	$ python3 


>> Acesso banco de dados
	>> Shell

from estoque.models import Autor
a1 = Autor(name="Sham Vinicius", idade="24")
a1.save()
a2 = Autor.objects.create(nome="Isabela Trix", idade="30")
Autor.objects.get(pk=2)
Autor.objects.first()
Autor.objects.last()
Autor.objects.all()

>>> Autor.objects.get(pk=1)
<Autor: Autor object (1)>
>>> Autor.objects.first()
<Autor: Autor object (1)>
>>> Autor.objects.last()
<Autor: Autor object (2)>
>>> Autor.objects.all()
<QuerySet [<Autor: Autor object (1)>, <Autor: Autor object (2)>]>
>>>

Autor.objects.filter(nome_icontains = 'Sham')
Autor.objects.filter(idade__lt = 29)
Autor.objects.filter(idade__gt = 25)
Autor.objects.filter(idade__lt = 30)
Autor.objects.exclude(idade__gt = 29)
Autor.objects.filter(idade__gt=29).update(idade=31)


>> Importando depdendencias
from estoque.models import Editora, Livro, Loja, Autor

# Criando Autores
a1 = Autor(name="Sham Vinicius", idade="24")
a1.save()
a2 = Autor.objects.create(nome="Isabela Trix", idade="30")

# Criando Editoras
e1 = Editora(nome="FTD", avaliacao=50)
e1.save()
e2 = Editora(nome="Peason", avaliacao=150)
e2.save()


editora1 = Editora.objects.get(nome="FTD")
editora2 = Editora.objects.get(nome="Pearson")


# Criando Lojas
l1 = Loja(nome='Loja 1', quantidade_de_clientes=10)
l1.save()
l2 = Loja(nome='Loja 2', quantidade_de_clientes=20)
l2.save()

# Buscando a DATA
from datetime import datetime
dt = datetime.now().date()


livro1 = Livro(paginas=100, nome="A tranças do rei careca", preco=20.00,avaliacao=9, editora=editora1, data_pub=dt)

livro2 = Livro(paginas=100,	nome="A volta dos que não fromram", preco=20.00,avaliacao=9, editora=editora2, data_pub=dt)

livro3 = Livro(paginas=100,	nome="Areia em alto mar", preco=20.00,avaliacao=9, editora=editora2, data_pub=dt)

livro1.autores.add(a1)
livro2.autores.add(a1) 
livro3.autores.add(a2)


Livro.objects.filter(
	editora__nome__in=["FTD", "Pearson"]
	)

>> Agregação

from django.db.models import Avg, Max, Min, Sum
Livro.objects.count()
Livro.objects.aggregate(qnt_paginas=Sum('paginas'))
Livro.objects.aggregate(preco_medio = Avg('preco'))
Livro.objects.aggregate(preco_max = Max('preco'))
Livro.objects.aggregate(preco_min = Min('preco'))

from django.db.models import F, Count

Autor.objects.



>>> Autor.objects.get(pk=1)
<Autor: Autor object (1)>
>>> Autor.objects.first()
<Autor: Autor object (1)>
>>> Autor.objects.last()
<Autor: Autor object (2)>
>>> Autor.objects.all()
<QuerySet [<Autor: Autor object (1)>, <Autor: Autor object (2)>]>
>>> 





