import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from core import settings
from .models import Mentorados, Navigators, DisponibilidadedeHorarios, Reuniao, Tarefa, Upload, ConsultaIA
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta
from .auth import valida_token
import locale
from django.db import transaction
from django.http import HttpResponseForbidden
from django.contrib import messages
import google.generativeai as genai
import logging
from django.conf import settings

# Configurar locale para português (ajuste conforme seu sistema)
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
    except:
        pass  # Fallback se não conseguir configurar

# Create your views here.
# Rota principal da página de mentorados
def mentorados(request):
    # Se o usuário não estiver logado, redireciona para a tela de login
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Se o usuário está apenas acessando a página (GET)
    if request.method == 'GET':
        # Filtra os Navigators e Mentorados do usuário logado
        navigators = Navigators.objects.filter(user=request.user)
        mentorados = Mentorados.objects.filter(user=request.user)

        # Renderiza a página HTML e envia os dados para ela
        return render(request, 'mentorados.html', {'navigators': navigators, 'mentorados': mentorados})
    
    # Se o usuário está enviando o formulário para cadastrar um mentorado (POST)
    elif request.method == 'POST':
        nome = request.POST.get('nome')              # Nome do mentorado
        foto = request.FILES.get('foto')             # Foto enviada
        estagio = request.POST.get("objetivo")       # Objetivo ou estágio
        navigator = request.POST.get('navigator')    # ID do navigator
        status = request.POST.get('status')          # Status inicial

        # Cria um novo objeto Mentorado com os dados do formulário
        mentorado = Mentorados(
            nome=nome,
            foto=foto,
            estagio=estagio,
            navigator_id=navigator,
            user=request.user,
            status=status
            
        )

        # Salva o mentorado no banco de dados
        mentorado.save()

        # Mostra uma mensagem de sucesso na tela
        messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso.')

        # Redireciona de volta para a mesma página
        return redirect('mentorados')
    

def reunioes(request):
    if request.method =='GET':
        reunioes_raw = Reuniao.objects.filter(data__mentor=request.user) #acesso uma outra propriedade de uma outra classe(então eu trago todas as reunioes desse do usuario)
        
        # Dicionário para mapear meses em português
        meses = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        
        # Formatação das reuniões para padrão brasileiro
        reunioes_formatadas = []
        for reuniao in reunioes_raw:
            # Cria uma cópia do objeto reunião
            reuniao_formatada = reuniao
            
            # Obtém a data/hora da disponibilidade
            data_hora = reuniao.data.data_inicial
            
            # Formata no padrão brasileiro: "5 de Abril de 2025 às 18:00"
            dia = data_hora.day
            mes = meses[data_hora.month]
            ano = data_hora.year
            hora = data_hora.strftime('%H:%M')
            
            # Adiciona o atributo formatado ao objeto
            reuniao_formatada.data_formatada = f"{dia} de {mes} de {ano} às {hora}"
            
            reunioes_formatadas.append(reuniao_formatada)
        
        return render(request, 'reunioes.html',{'reunioes': reunioes_formatadas})
    elif request.method == 'POST':
        data = request.POST.get('data')
        data = datetime.strptime(data, '%Y-%m-%dT%H:%M') #converter a 'str' para um objeto do tipo 'date'

        disponibilidades = DisponibilidadedeHorarios.objects.filter(mentor = request.user).filter(
            data_inicial__gte=(data - timedelta(minutes=50)),
            data_inicial__lte=(data + timedelta(minutes=50)),

        )

        if disponibilidades.exists():
            messages.add_message(request, constants.ERROR, 'Você já possui uma reunião em aberto!')
            return redirect('reunioes')

        disponibilidades = DisponibilidadedeHorarios(
            data_inicial=data,
            mentor=request.user,
        )

         
        disponibilidades.save()

        messages.add_message(request, constants.SUCCESS, 'Horário disponibilizado com sucesso!')
        return redirect('reunioes')
    
def auth(request):
    if request.method == 'GET':
       #print(request.COOKIES)
        return render(request, 'auth_mentorado.html')
    elif request.method == 'POST':
        token = request.POST.get('token')

    if not Mentorados.objects.filter(token=token).exists():
        messages.add_message(request, constants.ERROR, 'Token Inválido!' )
        return redirect ('auth_mentorado')
    
    response = redirect('escolher_dia')
    response.set_cookie('auth_token', token, max_age=4000)
        
    return response

def escolher_dia(request):
    if not valida_token(request.COOKIES.get('auth_token')):
        #print("TOKEN NO COOKIE:", request.COOKIES.get('auth_token'))
        return redirect('auth_mentorado')
    
    if request.method == 'GET':
        #print(request.COOKIES.get('auth_token'))
        #return HttpResponse('teste')
        mentorado = valida_token(request.COOKIES.get('auth_token'))
        disponibilidades = DisponibilidadedeHorarios.objects.filter(
            data_inicial__gte=datetime.now(),
            agendado=False,
            mentor=mentorado.user 
        ).values_list('data_inicial', flat=True) # o flat coloca tudo direto numa lista, que estava dentro de uma tupla

        # Dicionário para mapear meses em português
        meses = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        
        # Dicionário para mapear dias da semana em português
        dias_semana = {
            0: 'Segunda-feira', 1: 'Terça-feira', 2: 'Quarta-feira',
            3: 'Quinta-feira', 4: 'Sexta-feira', 5: 'Sábado', 6: 'Domingo'
        }
        
        datas_formatadas = []
        datas_unicas = set()
        
        for data_hora in disponibilidades:
            data = data_hora.date()
            if data not in datas_unicas:
                datas_unicas.add(data)
                
                # Formatação com dia da semana e mês por extenso
                dia_semana = dias_semana[data.weekday()]
                dia = data.day
                mes = meses[data.month]
                ano = data.year
                
                data_formatada = f"{dia_semana}, {dia} de {mes}"
                data_original = data.strftime('%d-%m-%Y')  # Mantém formato original para URL
                
                datas_formatadas.append({
                    'data_formatada': data_formatada,
                    'data_original': data_original
                })
        
        # Ordenar por data
        datas_formatadas.sort(key=lambda x: datetime.strptime(x['data_original'], '%d-%m-%Y'))
        
        return render(request, 'escolher_dia.html', {'horarios': datas_formatadas})

def agendar_reuniao(request):
    # Valida o token do mentorado no cookie
    if not valida_token(request.COOKIES.get('auth_token')):
        return redirect('auth_mentorado')
    
    # Recupera o objeto do mentorado autenticado
    mentorado = valida_token(request.COOKIES.get('auth_token'))

    if request.method == 'GET':
        data = request.GET.get('data')
        data = datetime.strptime(data, '%d-%m-%Y')

        # Filtra horários disponíveis do próprio mentor (mentorado.user é o mentor)
        horarios = DisponibilidadedeHorarios.objects.filter(
            data_inicial__gte=data,
            data_inicial__lt=data + timedelta(days=1),
            agendado=False,
            mentor=mentorado.user
        )
        
        # Formatação dos horários para o template
        horarios_formatados = []
        for horario in horarios:
            hora_inicial = horario.data_inicial.strftime('%H:%M')
            hora_final = horario.data_final().strftime('%H:%M')

            horarios_formatados.append({
                'id': horario.id,
                'horario_formatado': f"{hora_inicial} - {hora_final}",
                'objeto_original': horario
            })
        
        return render(request, 'agendar_reuniao.html', {
            'horarios': horarios_formatados,
            'tags': Reuniao.tag_choices
        })

    else:  # POST
        horario_id = request.POST.get('horario')
        tag = request.POST.get('tag')
        descricao = request.POST.get('descricao')

        try:
            with transaction.atomic():
                # Busca o horário no banco (ou retorna 404 se não existir)
                horario = get_object_or_404(DisponibilidadedeHorarios, id=horario_id)

                # 🔐 VALIDAÇÃO: garante que o horário é de um mentor do mentorado
                if horario.mentor != mentorado.user:
                    return HttpResponseForbidden("Você não pode agendar esse horário.")

                # Cria e salva o objeto de reunião
                reuniao = Reuniao(
                    data_id=horario_id,
                    mentorado=mentorado,
                    tag=tag,
                    descricao=descricao
                )
                reuniao.save()

                # Marca o horário como agendado
                horario.agendado = True
                horario.save()

                messages.add_message(request, constants.SUCCESS, 'Reunião agendada com sucesso!')
                return redirect('escolher_dia')

        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Erro ao agendar reunião.')
            print("Erro na transação:", e)
            return redirect('agendar_reuniao')  # ou página de erro, se preferir




def tarefa(request, id):
    mentorado = Mentorados.objects.get(id=id)
    if mentorado.user != request.user:
        raise Http404
        
    if request.method == 'GET':
        tarefas = Tarefa.objects.filter(mentorado=mentorado)
        videos = Upload.objects.filter(mentorado=mentorado)
        return render(request, 'tarefa.html', {'mentorado': mentorado, 'tarefas': tarefas, 'videos': videos})
    else:
        tarefa = request.POST.get('tarefa')

        tarefa = Tarefa(
            mentorado=mentorado,
            tarefa=tarefa
        )
        tarefa.save()
        return redirect(f'/mentorados/tarefa/{mentorado.id}')
    


def deletar_tarefa(request, tarefa_id):
    """Exclui uma tarefa específica"""
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, id=tarefa_id)
        
        # Verifica se o usuário logado é o mentor responsável pelo mentorado
        if tarefa.mentorado.user != request.user:
            raise Http404
        
        mentorado_id = tarefa.mentorado.id
        tarefa.delete()
        
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect(f'/mentorados/tarefa/{mentorado_id}')
    
    raise Http404


def deletar_video(request, video_id):
    """Exclui um vídeo específico"""
    if request.method == 'POST':
        video = get_object_or_404(Upload, id=video_id)
        
        # Verifica se o usuário logado é o mentor responsável pelo mentorado
        if video.mentorado.user != request.user:
            raise Http404
        
        mentorado_id = video.mentorado.id
        
        # Remove o arquivo físico do servidor
        if video.video:
            video.video.delete(save=False)
        
        video.delete()
        
        messages.success(request, 'Vídeo excluído com sucesso!')
        return redirect(f'/mentorados/tarefa/{mentorado_id}')
    
    raise Http404


# Versões AJAX (opcional - para exclusão sem recarregar a página)
def deletar_tarefa_ajax(request, tarefa_id):
    """Exclui uma tarefa via AJAX"""
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, id=tarefa_id)
        
        if tarefa.mentorado.user != request.user:
            return JsonResponse({'success': False, 'error': 'Não autorizado'})
        
        tarefa.delete()
        return JsonResponse({'success': True, 'message': 'Tarefa excluída com sucesso!'})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})


def deletar_video_ajax(request, video_id):
    """Exclui um vídeo via AJAX"""
    if request.method == 'POST':
        video = get_object_or_404(Upload, id=video_id)
        
        if video.mentorado.user != request.user:
            return JsonResponse({'success': False, 'error': 'Não autorizado'})
        
        # Remove o arquivo físico do servidor
        if video.video:
            video.video.delete(save=False)
        
        video.delete()
        return JsonResponse({'success': True, 'message': 'Vídeo excluído com sucesso!'})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})


def upload(request, id):
    mentorado = Mentorados.objects.get(id=id)
    if mentorado.user != request.user:
        raise Http404
    
    video = request.FILES.get('video')
    upload = Upload(
        mentorado=mentorado,
        video=video

    )
    upload.save()
    return redirect(f'/mentorados/tarefa/{mentorado.id}')



from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

def tarefa_mentorado(request):
    mentorado = valida_token(request.COOKIES.get('auth_token'))
    if not mentorado:
        return redirect('auth_mentorado')
    
    if request.method == 'GET':
        videos = Upload.objects.filter(mentorado=mentorado)
        tarefas = Tarefa.objects.filter(mentorado=mentorado)
        
        # Cálculos para o painel de IA
        total_tarefas = tarefas.count()
        tarefas_concluidas = tarefas.filter(realizada=True).count()
        
        # Cálculo do progresso da trilha (percentual de tarefas concluídas)
        progresso_trilha = int((tarefas_concluidas / total_tarefas * 100)) if total_tarefas > 0 else 0
        
        # Recomendação simples baseada no progresso
        if progresso_trilha >= 80:
            recomendacao_ia = "Excelente progresso! Continue assim."
        elif progresso_trilha >= 50:
            recomendacao_ia = "Bom ritmo! Foque nas tarefas pendentes."
        elif progresso_trilha >= 20:
            recomendacao_ia = "Acelere o ritmo para melhor resultado."
        else:
            recomendacao_ia = "Comece pelas tarefas mais simples."
        
        # Data da última análise (atual)
        ultima_analise = datetime.now().strftime("%d/%m/%Y")
        
        context = {
            'mentorado': mentorado,
            'videos': videos,
            'tarefas': tarefas,
            'total_tarefas': total_tarefas,
            'tarefas_concluidas': tarefas_concluidas,
            'progresso_trilha': progresso_trilha,
            'recomendacao_ia': recomendacao_ia,
            'ultima_analise': ultima_analise,
        }
        
        return render(request, 'tarefa_mentorado.html', context)
 

@csrf_exempt
@require_http_methods(["POST"])
def assistente_ia(request):
    """
    View para processar dúvidas do mentorado usando IA
    """
    try:
        # Validar token do mentorado
        mentorado = valida_token(request.COOKIES.get('auth_token'))
        if not mentorado:
            return JsonResponse({'error': 'Token inválido'}, status=401)
        
        # Obter dados da requisição
        data = json.loads(request.body)
        duvida = data.get('duvida', '').strip()
        
        if not duvida:
            return JsonResponse({'error': 'Por favor, digite sua dúvida.'}, status=400)
        
        # Verificar se a API key está configurada
        if not settings.GEMINI_API_KEY:
            return JsonResponse({'error': 'API key não configurada'}, status=500)
        
        # Configurar o modelo Gemini
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Criar prompt personalizado para mentoria
        prompt = f"""
        Você é um assistente de mentoria educacional. Um mentorado tem a seguinte dúvida:
        
        "{duvida}"
        
        Forneça uma resposta educativa, clara e prática que:
        1. Explique o conceito de forma simples
        2. Dê exemplos práticos
        3. Sugira uma atividade ou exercício para praticar
        4. Mantenha um tom encorajador e motivacional
        
        Limite sua resposta a no máximo 200 palavras.
        """
        
        # Gerar resposta da IA
        response = model.generate_content(prompt)
        resposta_ia = response.text
        
        # Salvar o histórico da consulta
        ConsultaIA.objects.create(
            mentorado=mentorado,
            duvida=duvida,
            resposta=resposta_ia
        )
        
        return JsonResponse({
            'sucesso': True,
            'resposta': resposta_ia,
            'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Dados inválidos'}, status=400)
    except Exception as e:
        # Log do erro para debug
        logging.error(f"Erro no assistente IA: {str(e)}")
        return JsonResponse({
            'error': f'Erro ao processar sua dúvida: {str(e)}'
        }, status=500)
    

@csrf_exempt  # Desativa temporariamente a verificação CSRF (só use se necessário e com segurança)
def tarefa_alterar(request, id):
    # 1. Verifica se o usuário (mentorado) está autenticado pelo token salvo nos cookies
    mentorado = valida_token(request.COOKIES.get('auth_token'))

    if not mentorado:
        # Se o token for inválido ou ausente, redireciona para a tela de login do mentorado
        return redirect('auth_mentorado')

    # 2. Busca a tarefa pelo ID. Se não existir, retorna erro 404 automaticamente
    tarefa = get_object_or_404(Tarefa, id=id)

    # 3. Verifica se a tarefa pertence ao mentorado autenticado
    if tarefa.mentorado != mentorado:
        # Se a tarefa não for do mentorado, proíbe o acesso (status HTTP 403)
        return HttpResponseForbidden("Você não tem permissão para alterar esta tarefa.")

    # 4. Altera o status da tarefa: se estava marcada como realizada, desmarca; se não estava, marca
    tarefa.realizada = not tarefa.realizada

    # 5. Salva a alteração no banco de dados
    tarefa.save()

    # 6. Retorna uma resposta simples indicando que a tarefa foi alterada com sucesso
    return HttpResponse("Tarefa atualizada com sucesso!")




    '''
        reuniao = Reuniao(
            data_id=horario_id,
            mentorado=mentorado,
            tag=tag,
            descricao=descricao
        )
        reuniao.save()

        horario = DisponibilidadedeHorarios.objects.get(id=horario_id)
        horario.agendado = True
        horario.save()
    '''

#O que é uma requisição AJAX?
#É uma requisição feita em segundo plano (sem recarregar a página) pelo navegador para o servidor. No nosso caso, o navegador envia dados para o servidor com JavaScript e espera uma resposta em JSON (um tipo de dado leve e fácil de usar).

@csrf_exempt  # Desativa proteção CSRF só para esta função (recomenda-se usar com cuidado)
@require_http_methods(["PATCH"])  # Só aceita requisições HTTP do tipo PATCH
def update_mentorado_status(request, id):
    try:
        # Imprime no terminal (debug)
        print("PATCH RECEBIDO")
        print(request.body)

        # Converte os dados JSON recebidos em um dicionário Python
        data = json.loads(request.body)
        status = data.get('status')  # Pega o novo status enviado

        print("Status recebido:", status)

        # Verifica se o status é um dos valores válidos
        if status not in ['ativo', 'inativo', 'pausado']:
            return JsonResponse({'success': False, 'error': 'Status inválido.'}, status=400)

        # Busca no banco de dados o mentorado com o ID fornecido
        mentorado = get_object_or_404(Mentorados, id=id)

        # Atualiza o campo status com o novo valor
        mentorado.status = status
        mentorado.save()  # Salva a alteração no banco de dados

        print("Status salvo com sucesso!")

        # Retorna uma resposta em JSON dizendo que deu tudo certo
        return JsonResponse({'success': True})

    except Exception as e:
        # Se der erro, imprime no terminal e envia erro como resposta
        print("Erro:", e)
        return JsonResponse({'success': False, 'error': str(e)}, status=500)