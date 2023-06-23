from django.db import models

nivel = [('1', 'Básico'), ('2', 'Intermediário'), ('3', 'Avançado')]

# contatos dos leads 
class Lead(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    nivel = models.CharField(max_length=1, choices=nivel)