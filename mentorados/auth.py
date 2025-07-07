from .models import Mentorados

def valida_token(token):  #Ela vai receber o valor do cookies do usuário e vai verificar se é um token válido(de um usuário). Pra ver se é válido, é ser ele estiver no banco de dados
    return Mentorados.objects.filter(token=token).first() #Caso não exista nenhum mentorado, ela retorna uma lista vazia 'none', caso retorne, é válido
 