from django.db import models

# Create your models here.
class Estudantes(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, primary_key=True)
    email = models.EmailField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)


    def __str__(self):
            return self.nome


class Curso(models.Model):
      NIVEL = (
            ('B', "Basico"),
            ('I', "Intermediario"),
            ('A', "Avançado"),
      )
      codigo = models.CharField(max_length=14)
      descricao = models.CharField(max_length=100, blank=False)
      nivel = models.CharField(max_length=1, choices = NIVEL, blank=False, null = False,default='B' )

      def __str__(self):
            return self.codigo

      
    