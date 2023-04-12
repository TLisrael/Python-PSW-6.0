from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    criador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=256)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    carga_horaria = models.IntegerField()
    logo = models.ImageField(upload_to="logos")
    
    participantes = models.ManyToManyField(User, related_name='evento_participante', blank=True, null=True)
    
    # paleta de cores 
    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)
    
    def __str__(self) -> str:
        return self.nome