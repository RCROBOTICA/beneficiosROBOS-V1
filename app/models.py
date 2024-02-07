from django.db import models


# Create your models here.



class Registro(models.Model):
    protocolo = models.CharField(max_length=100)
    solicitacao = models.CharField(max_length=100)
    a = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    r = models.CharField(max_length=100)
    nc = models.CharField(max_length=100)
    lm = models.CharField(max_length=100)




