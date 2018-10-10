from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cadastro(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=10)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    aniversario = models.DateField()

    priority_list = (
        ('0', 'Feminino'),
        ('1', 'Masculino'),
    )

    priorities_list = (
        ('0', 'Casado'),
        ('1', 'Solteiro'),
        ('2', 'Namorando'),
        ('3', 'Viúva'),
        ('4', 'A espera de um milagre'),
    )

    sexo = models.CharField(max_length=1, choices=priority_list)
    estado_civil = models.CharField(max_length=1, choices=priorities_list)

    def __str__(self):
        return self.nome