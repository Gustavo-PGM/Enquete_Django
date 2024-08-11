from django.shortcuts import render
from .models import Pergunta, Escolher
# Create your views here.


def enquetes(request):
    template_name = 'enquetes.html'
    perguntas = Pergunta.objects.all()
    contexto = {
        'perguntas':perguntas
    }
    return render(request, template_name, contexto)


def votos(request, pk):
    template_name = 'votos.html'
    questao = Pergunta.objects.get(id=pk)
    opcoes = questao.escolhas.all()

    contexto = {
        'questao':questao,
        'opcoes': opcoes
    }

    return render(request, template_name, contexto)


def resultados(request, pk):
    template_name = 'resultados.html'
    questao = Pergunta.objects.get(id=pk)
    opcoes = questao.escolhas.all()
    if request.method == 'POST':
        valor = request.POST['resposta'] #Valor do input, cujo nome 'resposta'
        opcao_selecionada =opcoes.get(id=valor)
        opcao_selecionada.votos += 1
        opcao_selecionada.save()

    contexto = {
        'questao':questao,
        'opcoes': opcoes
    }

    return render(request, template_name, contexto)