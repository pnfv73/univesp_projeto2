from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Tabela pessoa
    # Caso seja feita uma implementação de herança de tabelas, a tabela pessoa deverá conter os campos id, email, password e papel
    id = models.AutoField(primary_key=True) #chave primária
    email = models.EmailField(unique=True)
    papel = models.CharField(max_length=1, null=False, blank=False, default='U') # papéis: (F) Funcionário e (U) Usuário    
    
    # Campos específicos para funcionários
    registro_funcional = models.CharField(max_length=10, null=True, blank=True) 
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    admin = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)
    
    # Campos de auditoria
    date_joined = models.DateTimeField(auto_now_add=True) 
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    








