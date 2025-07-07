from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentorados, name='mentorados'),  # Página principal com a lista e formulário
    path('api/mentorados/<int:id>/status/', views.update_mentorado_status, name='update_mentorado_status'),  # Rota da API usada pelo JavaScript para trocar o status do mentorado sem recarregar a página
    path('reunioes/', views.reunioes, name='reunioes'),
    path('auth/', views.auth, name="auth_mentorado"),
    path('escolher_dia/', views.escolher_dia, name='escolher_dia'),
    path('agendar_reuniao/', views.agendar_reuniao, name='agendar_reuniao'),
    path('tarefa/<int:id>', views.tarefa, name='tarefa'),
    path('upload/<int:id>', views.upload, name='upload'),
    path('tarefa_mentorado/', views.tarefa_mentorado, name='tarefa_mentorado'),
    path('tarefa_alterar/<int:id>', views.tarefa_alterar, name="tarefa_alterar"),

    # Novas URLs para exclusão
    path('deletar_tarefa/<int:tarefa_id>/', views.deletar_tarefa, name='deletar_tarefa'),
    path('deletar_video/<int:video_id>/', views.deletar_video, name='deletar_video'),
    
    # URLs AJAX (opcional)
    path('ajax/deletar_tarefa/<int:tarefa_id>/', views.deletar_tarefa_ajax, name='deletar_tarefa_ajax'),
    path('ajax/deletar_video/<int:video_id>/', views.deletar_video_ajax, name='deletar_video_ajax'),

    # Nova URL para o assistente de IA
    path('assistente-ia/', views.assistente_ia, name='assistente_ia'),
    
]




        
