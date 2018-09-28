from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from estoque.models import Autor, Livro, Editora, Loja
from django.urls import reverse_lazy
from django.db.models import Avg
from django import forms
from django.views.generic.edit import FormMixin
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# from django.http import HttpResponse

class PageInfoMixin(object):
	page_info = None

	def get_page_info(self):
		if self.model:
			return None

	def get_context_data(self, **kwargs):
		if self.page_info is None:
			kwargs['page_info'] = self.get_page_info()
		return super().get_context_data(**kwargs)


@login_required(login_url='accounts/login')
def index(request):
	return render(request, 'estoque/index.html', {
		'abacate': True,
		'default': None
		})

#	AUTORES

class AutorListView(ModelFormMixin, ListView):
	fields = '__all__'
	model = Autor
	templete_name = 'estoque/autor_list.html'

	def get(self, request, *args, **kwargs):
		self.object = None
		return super().get(request, *args, **kwargs)

class AutorCreateView(CreateView):
	model = Autor
	fields = '__all__'
	success_url = reverse_lazy('autor-list')

	def form_valid(self, form):
		if self.request.is_ajax():
			obj = form.save()
			return JsonResponse({
				'obj': {'nome': obj.nome, 'idade': obj.idade,
				}
			})
		return super().form_valid(form)


	def form_invalid(self, form):
		if self.request.is_ajax():
			return JsonResponse({
				'errors': form.errors, 'non_field_errors':form.non_field_errors()
				})
		return super().form_invalid(form)

class AutorUpdateView(UpdateView):
	model = Autor
	fields = '__all__'
	success_url = reverse_lazy('autor-list')


class AutorDeleteView(DeleteView):
	model = Autor
	success_url = reverse_lazy('autor-list')

#	LIVRO

class LivroListView(ListView):
	model = Livro
	templete_name = 'estoque/autor_list.html'
	

class LivroUpdateView(UpdateView):
	model = Livro
	fields = '__all__'
	success_url = reverse_lazy('livro-list')


class LivroDeleteView(DeleteView):
	model = Livro
	success_url = reverse_lazy('livro-list')


class LivroForm(forms.ModelForm):
	def get_avaliacao_avg(self):
		livros = Livro.objects.filter(autores__in=self.cleaned_data['autores']).distinct()
		media = livros.aggregate(Avg('avaliacao'))
		return media.get('avaliacao__avg', 0)

	def save(self, commit=True):
		instance = super().save(commit=False)
		if commit:
			instance.avaliacao = self. get_avaliacao_avg()
			instance.save()
			self.save_m2m()
		return instance

	class Meta:
		model = Livro
		fields = ['nome', 'paginas', 'preco', 'autores', 'editora', 'data_pub']


class LivroCreateView(CreateView):
	model = Livro
	form_class = LivroForm
	#fields = '__all__'
	success_url = reverse_lazy('livro-list')

#	ListView de Busca

class SearchFormListView(FormMixin, ListView):
	def get(self, request, *args, **kwargs):
		self.form = self.get_form(self.get_form_class())
		self.object_list = self.form.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list, form=self.form))

	def get_form_kwargs(self):
		return {'initial':self.get_initial(), 'data': self.request.GET}

class LivroSearchForm(forms.Form):
	nome = forms.CharField(required=False)
	autores = forms.CharField(required=False)
	editora = forms.ModelChoiceField(required=False, queryset=Editora.objects)

	def get_queryset(self):
		q = Q()
		if self.is_valid():
			if self.cleaned_data.get('nome'):
				q = q & Q(nome__icontains=self.cleaned_data['nome'])
			if self.cleaned_data.get('autores'):
				q = q & Q(nome__icontains=self.cleaned_data['autores'])
			if self.cleaned_data.get('editora'):
				q = q & Q(nome__icontains=self.cleaned_data['editora'])
		return Livro.objects.filter(q)

class LivroSearchFormView(PageInfoMixin, SearchFormListView):
	form_class = LivroSearchForm
	model = Livro
	template_name = 'estoque/livro_search.html'


	def get_page_info(self):
		return 'Livros: %s' %(Livro.objects.count())
	
#	EDITORAS

class EditoraListView(ListView):
	model = Editora
	templete_name = 'estoque/editoras_list.html'


class EditoraCreateView(CreateView):
	model = Editora
	fields = '__all__'
	success_url = reverse_lazy('editoras-list')


class EditoraUpdateView(UpdateView):
	model = Editora
	fields = '__all__'
	success_url = reverse_lazy('editoras-list')


class EditoraDeleteView(DeleteView):
	model = Editora
	success_url = reverse_lazy('editoras-list')

#	LOJAS

class LojaListView(ListView):
	model = Loja
	templete_name = 'estoque/loja_list.html'


class LojaCreateView(CreateView):
	model = Loja
	fields = '__all__'
	success_url = reverse_lazy('loja-list')


class LojaUpdateView(UpdateView):
	model = Loja
	fields = '__all__'
	success_url = reverse_lazy('loja-list')


class LojaDeleteView(DeleteView):
	model = Loja
	success_url = reverse_lazy('loja-list')

class JsonListMixin(object):
	json_fields = []

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset().values_list(*self.json_fields)
		json_dict = {
			'header': self.json_fields,
			'object_list': list(self.object_list)
		}
		return JsonResponse(json_dict)

class LivroJsonListView(JsonListMixin, LivroListView):
	json_fields = [
		'nome',
		'paginas',
		'preco',
		'avaliacao',
		'editora__nome',
		'autores__nome',
	]


def autor_nome_registrado(request):
	#import pdb; pdb.set_trace()

	nome = request.GET.get('nome', None)

	data = {
		'is_taken': Autor.objects.filter(nome__iexact=nome).exists()
	}
	if data['is_taken']:
		data['error_message'] = ' O autor já está cadastrado'

	return JsonResponse(data)

