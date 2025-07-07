from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta #Cria um intervalo de tempo
import secrets 
from django.utils import timezone


class Navigators(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Mentor

    def __str__(self):
        return self.nome


# Create your models here.
class Mentorados(models.Model):
    '''estagio_choices = (
        ('E1', '10-100k'),
        ('E2', '100-1kk')


    )'''
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('pausado', 'Pausado'),
    ]

    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True) #As fotos vão ser opcionais 
    estagio = models.CharField(max_length=100) #choices=estagio_choices / # campo onde eu posso adicionar textos ali dentro, conjunto de caracteres, mas esses caracteres são especificos, escolidos pelos usuarios
    navigator = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #ForeignKey: Relação com 2 tabelas / CASCADE: se o mentor for deletado, todos os mentorados tbm serão # O user = Mentor
    criado_em = models.DateField(auto_now_add=True) #Vai ser automaticamente salvo com a data no momento que o mentorado foi salvo
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')
    token = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.gerar_token_unico()  #secrets.token_urlsafe(8)
        super().save(*args, **kwargs)  #Super sempre se referencia a classe mãe, a classe herdada(Model)

    def gerar_token_unico(self):
        while True:
            token = secrets.token_urlsafe(8)
            if not Mentorados.objects.filter(token=token).exists():
                return token

    def __str__(self):
        return self.nome 
    

class DisponibilidadedeHorarios(models.Model):

    # Data e hora de início da disponibilidade
    # null=True permite que o campo seja nulo no banco de dados
    # blank=True permite que o campo seja deixado em branco em formulários
    data_inicial = models.DateTimeField(null=True, blank=True)

    # Relaciona esta disponibilidade com o usuário (mentor) que criou
    # Se o usuário for deletado, todas as disponibilidades associadas a ele também serão excluídas
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)

    # Indica se esse horário já foi agendado ou ainda está disponível
    # Por padrão, o valor é False (ou seja, disponível)
    agendado = models.BooleanField(default=False)


    def data_final(self):
        return self.data_inicial + timedelta(minutes=50)
    

class Reuniao(models.Model):
    tag_choices = (
        ('G', 'Gestão'),
        ('M', 'Marketing'),
        ('RH', 'Gestão de pessoas'),
        ('I', 'Impostos'),
        ('DA', 'Dificuldade em Aprendizagem'),
        ('D', 'Dúvidas Gerais')
    )
    
    data = models.ForeignKey(DisponibilidadedeHorarios, on_delete=models.CASCADE)
    mentorado = models.ForeignKey(Mentorados, on_delete=models.CASCADE)
    tag = models.CharField(max_length=2, choices=tag_choices)
    descricao = models.TextField()

    def __str__(self):
        return f"Reunião: {self.mentorado.nome} - {self.get_tag_display()}"
    
    class Meta:
        verbose_name = "Reunião"
        verbose_name_plural = "Reuniões"


class Tarefa(models.Model):
    mentorado = models.ForeignKey(Mentorados, on_delete=models.DO_NOTHING)
    tarefa = models.CharField(max_length=255)
    realizada = models.BooleanField(default=False)


class Upload(models.Model):
    mentorado = models.ForeignKey(Mentorados, on_delete=models.DO_NOTHING)
    video = models.FileField(upload_to='video')


class ConsultaIA(models.Model):
    mentorado = models.ForeignKey('Mentorados', on_delete=models.CASCADE)
    duvida = models.TextField()
    resposta = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Consulta IA'
        verbose_name_plural = 'Consultas IA'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.mentorado} - {self.duvida[:50]}..."

    #python manage.py makemigrations ("criei classes, essas classes são tabelas do banco, gere essas tabelas")-0001 no migrations
    #python manage.py migrate ("Leia aqueles arquivos de migração, e aqueles que não foram aplicados ainda, aplique") - criou tabelas novas
    #("criar um usuario 'admin' para acessar a URL admin")- admin 123

    #para delete (del db.sqlite3

    #resetar ou excluir tabelas (1. python manage.py dbshell, 2. DROP TABLE nome_da_tabela;, 3.  .quit)

'''Você pode:

Aumentar a largura da coluna com o mouse (arrastando na interface do SQLite Viewer).

Rodar um comando SQL manualmente no terminal usando o dbshell: python manage.py dbshell / E dentro dele, execute: PRAGMA table_info(mentorados_disponibilidadedehorarios);'''



