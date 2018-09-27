from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('autores/',views.AutorListView.as_view(), name='autor-list'),
	path('autores/novo/', views.AutorCreateView.as_view(), name="autor-create"),
	path('autores/update/<int:pk>/', views.AutorUpdateView.as_view(), name='autor-update'),
	path('autores/remove/<int:pk>/', views.AutorDeleteView.as_view(), name="autor-delete"),
	
	#	Verificar Disponibilidade Autor
	#	http://127.0.0.1:8000/autores/taken/?nome=Sham
	path('autores/taken/', views.autor_nome_registrado, name='autor-taken'),

	path('livros/',views.LivroListView.as_view(), name='livro-list'),
	path('lviros/novo/', views.LivroCreateView.as_view(), name="livro-create"),
	path('livros/update/<int:pk>/', views.LivroUpdateView.as_view(), name='livro-update'),
	path('livros/remove/<int:pk>/', views.LivroDeleteView.as_view(), name="livro-delete"),

	#	Buscar Livros Json
	path('livros.json/', views.LivroJsonListView.as_view(), name="livro-json-list"),
	
	#	Buscar Livros
	path('livros/search/', views.LivroSearchFormView.as_view(), name='livro-search'),

	path('editoras/',views.EditoraListView.as_view(), name='editora-list'),
	path('editoras/novo/', views.EditoraCreateView.as_view(), name="editora-create"),
	path('editoras/update/<int:pk>/', views.EditoraUpdateView.as_view(), name='editora-update'),
	path('editoras/remove/<int:pk>/', views.EditoraDeleteView.as_view(), name="editora-delete"),

	path('lojas/',views.LojaListView.as_view(), name='loja-list'),
	path('lojas/novo/', views.LojaCreateView.as_view(), name="loja-create"),
	path('lojas/update/<int:pk>/', views.LojaUpdateView.as_view(), name='loja-update'),
	path('lojas/remove/<int:pk>/', views.LojaDeleteView.as_view(), name="loja-delete"),

]

