from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from app.models import Registro
from django.http import HttpResponse
from app.forms import RegistroForm



# FUNÇÃO DA PAGINA PRINCIPAL
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data = Registro.objects.filter(protocolo=search)
    else:
        search = '';
    # else:
    #     data = Registro.objects.all()
    dados = {'data': data, 'search': search}
    return render(request, 'index.html', dados)

# FUNÇÃO DA PAGINA DO ADMINISTRADOR
def home_2(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data = Registro.objects.filter(protocolo=search)
    else:
        data = Registro.objects.all()
    dados = {'data': data, 'search': search}
    return render(request, 'adm.html', dados)

def form(request):
     data = {}
     data['form'] = RegistroForm()
     return render(request, 'form.html', data)

def salvarCli(request):
     form = RegistroForm(request.POST or None)
     if form.is_valid():
          form.save()
     return redirect('/')

def view(request, pk):
    data = {}
    data['db'] = Registro.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Registro.objects.get(pk=pk)
    data['form'] = RegistroForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Registro.objects.get(pk=pk)
    form = RegistroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('/')

def delete(request, pk):
    db = Registro.objects.get(pk=pk)
    db.delete()
    return redirect('home_2')

# ------------------------AS FUNÇÕES A BAIXO FAZEM PARTE DAS EXPLICAÇÕES DE CADA STATUS -----------------------------------
def protocolo(request):
    return render(request, 'protocolo.html')

def solicitacao(request):
    return render(request, 'solicitacao.html')

def analise(request):
    return render(request, 'analise.html')

def contemplado(request):
    return render(request, 'contemplado.html')

def nao_contemplado(request):
    return render(request, 'nao_contemplado.html')

def lista_medicao(request):
    return render(request, 'lista_medicao.html')

def recebido(request):
    return render(request, 'recebido.html')

# ------------------------------------------------------


# Create your views here.
