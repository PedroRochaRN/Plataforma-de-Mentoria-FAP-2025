from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate #recebe as credenciais do usuarios e verifica se esses dados existem no banco de dados ou não, se existir, retornar o próprio usuário, senão, retorna none(vazio)
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')                     #HttpResponse('Olá Mundo')
    elif request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email') 
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm_password')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha e confirmar senha, devem ser iguais.')
            return redirect('/usuarios/cadastro/')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter 6 ou mais caracteres.')
            return redirect('/usuarios/cadastro/')

        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse username.')
            return redirect('/usuarios/cadastro/')
        
        User.objects.create_user(
            username = username,
            email = email,
            password = senha

        )

        return redirect('/usuarios/login/')
        #return HttpResponse(f'{username} - {email} - {senha} - {confirmar_senha}')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username = username, password = senha)

        if user:
            auth .login(request, user)
            return redirect('/mentorados/')
        
        messages.add_message(request, constants.ERROR, 'Nome ou Senha Inválidos.')
        return redirect('login')

