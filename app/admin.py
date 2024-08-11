from django.contrib import admin
from .models import Pergunta, Escolher

class EscolherInline(admin.TabularInline):
    model = Escolher
    extra = 4

class PerguntaAdm(admin.ModelAdmin):
    list_display = ['pergunta', 'usuario', 'criada_em']
    inlines = [EscolherInline]

class EscolherAdm(admin.ModelAdmin):
    list_display = ['opcao', 'votos']

admin.site.register(Pergunta, PerguntaAdm)
admin.site.register(Escolher, EscolherAdm)
