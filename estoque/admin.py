from django.contrib import admin

from django.contrib import admin

from .models import Livro, Autor, Editora, Loja

admin.site.register(Livro)

admin.site.register(Autor)

admin.site.register(Editora)

admin.site.register(Loja)