from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pergunta(models.Model):
    pergunta = models.CharField(max_length=150, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pergunta

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'
        ordering = ['criada_em']

class Escolher(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='escolhas') #Conectei a pergunta com a escolha
    opcao = models.CharField(max_length=100, null=False)
    votos = models.IntegerField(default=0)


    class Meta:
        verbose_name = 'Opcões'
        verbose_name_plural = 'Opcões'
        ordering = ['id']