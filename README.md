# MentorBook - Plataforma de Mentoria com IA

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://djangoproject.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📌 Visão Geral

O **MentorBook** é uma plataforma web construída com Django que conecta mentores a mentorados, permitindo o gerenciamento de tarefas, vídeos, agendamento de reuniões e interação com uma inteligência artificial (IA) para suporte educacional.

🎬 Vídeos Demonstrativos
📹 Vídeo 1: Apresentação e Configuração Inicial

Foco: Apresentação do projeto + Instalação do ambiente virtual e servidor

Conteúdo abordado:

Apresentação geral do projeto MentorBook
Instalação e configuração do ambiente virtual Python
Configuração das dependências do projeto
Inicialização do servidor Django
Primeiro contato com a aplicação

🔗 Link do Vídeo: [Inserir link aqui]

📹 Vídeo 2: Estrutura Django e Plataforma do Mentor

Foco: Explicação da estrutura Django + Demonstração da interface do mentor

Conteúdo abordado:

Estrutura completa de um projeto Django
Criação e organização de apps Django
Sistema de roteamento e definição de URLs
Conexão entre views, templates e models
Demonstração prática da plataforma do mentor
Lógica por trás da arquitetura Django aplicada ao projeto

🔗 Link do Vídeo: [Inserir link aqui]

📹 Vídeo 3: Código e Funcionalidades na Prática

Foco: Demonstração técnica do código + Funcionalidades visuais da plataforma

Conteúdo abordado:

Análise detalhada do código-fonte
Explicação das funcionalidades implementadas
Demonstração visual das páginas da aplicação
Como o sistema funciona na prática
Interface do mentorado e do mentor
Funcionalidades de IA, tarefas, vídeos e reuniões
Fluxo completo de uso da plataforma

🔗 Link do Vídeo: [Inserir link aqui]

## ⚡ Quick Start
```bash
git clone https://github.com/seu-usuario/mentorbook.git
cd mentorbook
pip install -r requirements.txt
cp .env.example .env  # Configure sua GEMINI_API_KEY
python manage.py migrate
python manage.py runserver
```

---

## 📂 Estrutura de Arquivos

```
mentorbook/
├── .vscode/                 # Configurações do VS Code
├── core/                    # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py          # Configurações Django + Gemini API
│   ├── urls.py              # URLs principais
│   ├── wsgi.py              # Configuração WSGI
│   └── asgi.py              # Configuração ASGI
├── usuarios/                # App de autenticação
│   ├── __pycache__/         # Cache Python
│   ├── migrations/          # Migrações do banco
│   ├── static/              # Arquivos estáticos
│   ├── templates/           # Templates de login/cadastro
│   │   ├── cadastro.html
│   │   └── login.html
│   ├── __init__.py
│   ├── admin.py             # Configuração Django Admin
│   ├── apps.py              # Configuração do app
│   ├── models.py            # Models de usuário
│   ├── tests.py             # Testes unitários
│   ├── urls.py              # URLs de autenticação
│   └── views.py             # Views de cadastro e login
├── mentorados/              # App principal
│   ├── __pycache__/         # Cache Python
│   ├── migrations/          # Migrações do banco
│   ├── templates/           # Templates principais
│   │   └── base.html        # Template base
│   ├── __init__.py
│   ├── admin.py             # Configuração Django Admin
│   ├── apps.py              # Configuração do app
│   ├── auth.py              # Validação de tokens
│   ├── models.py            # Models do banco de dados
│   ├── tests.py             # Testes unitários
│   ├── urls.py              # URLs do app
│   └── views.py             # Lógica de mentores/mentorados
├── templates/               # Templates globais
│   └── base.html            # Template base global
├── media/                   # Arquivos de upload
│   ├── fotos/               # Fotos dos mentorados
│   └── videos/              # Vídeos educativos
├── .env                     # Variáveis de ambiente (não versionar)
├── .gitignore               # Arquivos ignorados pelo Git
├── db.sqlite3               # Banco de dados SQLite
├── main.py                  # Arquivo principal/auxiliar
├── manage.py                # Gerenciador Django
├── README.md                # Documentação do projeto
├── roteiro.txt              # Documentação adicional/roteiro
└── requirements.txt         # Dependências do projeto
```

---

## 📝 Detalhamento dos Diretórios

### **📁 Core (Configurações Django):**
- **`settings.py`** - Configurações principais + integração Google Gemini
- **`urls.py`** - Roteamento principal da aplicação
- **`wsgi.py`** - Configuração para servidor WSGI
- **`asgi.py`** - Configuração para servidor ASGI

### **👤 Usuarios (Autenticação):**
- **`models.py`** - Model de usuário personalizado
- **`views.py`** - Lógica de cadastro e login
- **`urls.py`** - URLs de autenticação
- **`templates/`** - Templates de login/cadastro
- **`static/`** - CSS/JS específicos de autenticação

### **🎓 Mentorados (App Principal):**
- **`models.py`** - Models: Mentorados, Tarefas, Uploads, Reuniões, etc.
- **`views.py`** - Lógica principal da aplicação
- **`auth.py`** - Sistema de validação de tokens
- **`urls.py`** - URLs do sistema de mentoria
- **`templates/`** - Templates do sistema principal

### **📄 Templates (Globais):**
- **`base.html`** - Template base com Tailwind CSS + Material Design
- Templates compartilhados entre apps

### **📁 Media (Uploads):**
- **`fotos/`** - Fotos de perfil dos mentorados
- **`videos/`** - Vídeos educativos enviados pelos mentores

### **⚙️ Configuração:**
- **`.env`** - Chave API Google Gemini + configurações sensíveis
- **`.gitignore`** - Arquivos/pastas ignorados pelo Git
- **`requirements.txt`** - Dependências Python do projeto

### **📊 Banco de Dados:**
- **`db.sqlite3`** - Banco SQLite com todos os dados
- **`migrations/`** - Histórico de mudanças no banco

---

## 🔧 Arquivos de Desenvolvimento

### **VS Code:**
- **`.vscode/`** - Configurações específicas do editor
- Configurações de debugging e extensões

### **Python:**
- **`__pycache__/`** - Cache Python (gerado automaticamente)
- **`main.py`** - Arquivo auxiliar/script principal
- **`manage.py`** - Gerenciador Django padrão

### **Documentação:**
- **`README.md`** - Documentação completa do projeto
- **`roteiro.txt`** - Roteiro de desenvolvimento/notas

---

## 🚀 Estrutura Modular

### **Separação de Responsabilidades:**
- **`core/`** - Configurações centrais
- **`usuarios/`** - Autenticação e gestão de usuários
- **`mentorados/`** - Lógica principal de mentoria
- **`templates/`** - Interface do usuário
- **`media/`** - Conteúdo multimedia

### **Organização Django:**
- Cada app tem sua própria pasta `templates/`
- Arquivos estáticos organizados por app
- Migrações isoladas por aplicação
- Models distribuídos logicamente

### **Boas Práticas:**
- Separação de templates globais e específicos
- Configurações sensíveis em `.env`
- Estrutura preparada para deploy
- Organização escalável e manutenível

---

## ⚙️ Tecnologias Utilizadas

- **Python 3** & **Django 5**  
- **HTML5 + TailwindCSS**  
- **HTMX** (requisições AJAX dinâmicas)  
- **Google Gemini AI API** (assistente inteligente educacional)  
- **SQLite** (banco de dados padrão)  
- **Material Design CSS** (interface amigável)  
- **Chart.js** (gráficos interativos)
- **python-dotenv** (gerenciamento de variáveis de ambiente)
- **Pillow** (processamento de imagens)

---

## 📊 Funcionalidades AJAX e Front-End

### **Componentes Externos:**
- **Material Design:** Icons + Roboto Font para UI moderna
- **Material-Components-Web:** Botões, inputs e responsividade
- **Chart.js:** Gráficos de progresso interativos
- **HTMX:** Formulários dinâmicos sem reload

### **Funcionalidades AJAX Implementadas:**
- **Alteração de Status:** Mudança de status do mentorado via PATCH
- **Marcação de Tarefas:** Toggle de conclusão instantâneo
- **Exclusão Inteligente:** Remoção de tarefas/vídeos via POST
- **Assistente IA:** Consultas em tempo real com resposta JSON
- **Validação Dinâmica:** Verificação de dados antes do envio
- **Requisições Assíncronas:** Interface responsiva sem recarregamento de página

---

## 🔐 Sistema de Autenticação

### Autenticação Dupla
O projeto implementa dois sistemas de autenticação distintos:

#### **Para Mentores:**
- **Cadastro Completo:**
  - Validação de senha (mínimo 6 caracteres)
  - Verificação de confirmação de senha
  - Validação de usuário único no sistema
  - Campos obrigatórios: username, email, password

- **Login Tradicional:**
  - Autenticação via username/password
  - Sessão Django padrão para manter usuário logado
  - Redirecionamento automático para dashboard após login
  
- **Segurança:**
  - Verificação de credenciais com `authenticate()`
  - Mensagens de erro para credenciais inválidas
  - Sistema de mensagens flash para feedback

#### **Para Mentorados:**
- **Acesso via Token:**
  - Token único de 8 caracteres gerado automaticamente
  - Geração com `secrets.token_urlsafe(8)` para máxima segurança
  - Validação de unicidade antes de salvar no banco
  - Autenticação via cookie `auth_token` com duração de 4000 segundos
  - Função `valida_token()` para verificar autenticidade
- **Segurança:**
  - Redirecionamento automático para login se token inválido
  - Validação de propriedade antes de qualquer operação
  - Proteção contra acesso a dados de outros mentores

---

## 👤 Funcionalidades Detalhadas

### **Para Mentores:**
- **Cadastro de Usuário:**
  - Sistema completo de registro com validações
  - Verificação de senha forte (mínimo 6 caracteres)
  - Confirmação de senha obrigatória
  - Validação de username único
- **Gerenciamento de Mentorados:**
  - Cadastro com foto, estágio, navigator e status
  - Sistema de status: **Ativo**, **Inativo**, **Pausado**
  - Alteração de status via AJAX (ativo/inativo/pausado)
  - Visualização de todos os mentorados em dashboard
  - Token único gerado automaticamente para cada mentorado
- **Sistema de Navigators:**
  - Cadastro e gerenciamento de navigators
  - Associação de mentorados a navigators específicos
  - Controle de acesso por mentor
- **Sistema de Tarefas:**
  - Criação, visualização e exclusão de tarefas
  - Exclusão via AJAX sem recarregar a página
  - Controle de permissões por mentor
  - Status de realização (pendente/concluída)
- **Gestão de Vídeos:**
  - Upload de vídeos educativos
  - Exclusão com remoção física do arquivo
  - Organização por mentorado
  - Suporte a diversos formatos de vídeo
- **Agendamento de Reuniões:**
  - Criação de disponibilidades com data/hora específica
  - Duração padrão de 50 minutos por reunião
  - Controle de horários já agendados
  - Visualização de todas as reuniões agendadas
  - Formatação automática em português brasileiro
  - Validação para evitar conflitos de horários
- **Dashboard Completo:**
  - Visão geral de todos os mentorados
  - Status de atividades em tempo real
  - Controle total das funcionalidades
  - Histórico de consultas IA dos mentorados

### **Para Mentorados:**
- **Acesso Seguro:**
  - Autenticação via token único de 8 caracteres
  - Validação rigorosa de permissões
  - Proteção contra acesso não autorizado

- **Visualização de Conteúdo:**
  - Tarefas atribuídas pelo mentor
  - Vídeos educativos organizados
  - Interface intuitiva e responsiva

- **Controle de Tarefas:**
  - Marcação como concluída/pendente via AJAX
  - Atualização instantânea sem recarregar página
  - Validação de propriedade da tarefa

- **Sistema de Reuniões:**
  - Visualização de datas disponíveis em português
  - Agendamento com seleção de horário e categoria

  - *Categorias disponíveis:*
    - **Gestão (G)**
    - **Marketing (M)**
    - **Gestão de Pessoas (RH)**
    - **Impostos (I)**
    - **Dificuldade em Aprendizagem (DA)**
    - **Dúvidas Gerais (D)**

  - Proteção contra agendamento com mentores incorretos
  - Validação de conflitos de horários
  - Campo de descrição obrigatório para contexto

- **Painel de Progresso:**
  - Cálculo automático de percentual de conclusão
  - Recomendações inteligentes baseadas no desempenho
  - Trilha de progresso visual com Chart.js
  - Estatísticas de tarefas concluídas vs pendentes

- **Assistente IA Avançado:**
  - Integração completa com Google Gemini AI
  - Perguntas educativas personalizadas
  - Histórico de consultas salvo automaticamente
  - Respostas limitadas a 200 palavras para concisão
  - Timestamp automático das consultas

---

## 🏆 Diferenciais do Projeto

- **IA Educacional:** Assistente personalizado com Google Gemini
- **Dual Authentication:** Sistema híbrido para mentores e mentorados
- **Tokens Seguros:** Geração com `secrets` e validação de unicidade
- **Interface Moderna:** Material Design + TailwindCSS
- **AJAX Completo:** Experiência fluida sem recarregamentos
- **Segurança Robusta:** Validações e proteções em todas as camadas
- **Português Nativo:** Formatação e localização brasileira
- **Escalabilidade:** Arquitetura preparada para crescimento
- **Documentação Completa:** Código comentado e README detalhado
- **Categorização Inteligente:** Sistema de navigators e tags de reunião
- **Histórico Completo:** Rastreamento de todas as atividades

---

## 🗃️ Modelos do Banco de Dados

### **Principais Models:**

#### **1. Mentorados:**
- **Campos:** nome, foto (opcional), estágio, navigator, mentor, data de criação, status, token
- **Status:** Ativo, Inativo, Pausado
- **Token:** Gerado automaticamente com `secrets.token_urlsafe(8)`
- **Funcionalidades:** Geração de token único, validação automática

#### **2. Navigators:**
- **Campos:** nome, mentor (relacionamento)
- **Relacionamento:** Cada navigator pertence a um mentor
- **Funcionalidade:** Organização e categorização de mentorados

#### **3. Tarefa:**
- **Campos:** mentorado, descrição da tarefa, status de realização
- **Funcionalidade:** Controle de tarefas atribuídas pelo mentor
- **Status:** Pendente (False) ou Concluída (True)

#### **4. Upload:**
- **Campos:** mentorado, arquivo de vídeo
- **Funcionalidade:** Armazenamento de conteúdo educativo
- **Localização:** Arquivos salvos em `media/video/`

#### **5. DisponibilidadedeHorarios:**
- **Campos:** data inicial, mentor, status de agendamento
- **Funcionalidade:** Cálculo automático de data final (50 minutos)
- **Controle:** Horários disponíveis vs agendados
- **Duração:** 50 minutos por reunião

#### **6. Reuniao:**
- **Campos:** data/horário, mentorado, categoria, descrição
- **Categorias:** 
  - **Gestão (G)**
  - **Marketing (M)** 
  - **Gestão de pessoas (RH)**
  - **Impostos (I)**
  - **Dificuldade em Aprendizagem (DA)**
  - **Dúvidas Gerais (D)**
- **Funcionalidade:** Organização e contexto das reuniões

#### **7. ConsultaIA:**
- **Campos:** mentorado, dúvida, resposta, timestamp
- **Funcionalidade:** Histórico completo de interações com IA
- **Ordenação:** Por data de criação (mais recente primeiro)
- **Integração:** Conecta com Google Gemini AI

---

## 🗄️ Configuração do Banco de Dados SQLite

O projeto utiliza **SQLite** como banco de dados padrão, que é automaticamente criado e gerenciado pelo Django.

### **Características do SQLite:**
- **Arquivo único:** Todo o banco fica no arquivo `db.sqlite3`
- **Zero configuração:** Não precisa instalar servidor de banco
- **Portável:** Pode ser facilmente copiado entre ambientes
- **Leve:** Ideal para desenvolvimento e projetos pequenos/médios
- **Integração nativa:** Suporte completo no Django

### **Localização do Banco:**
```
mentorbook/
├── db.sqlite3               # Arquivo do banco SQLite
├── manage.py
└── ...
```

### **Gerenciamento Automático:**
- **Criação automática:** O Django cria o arquivo na primeira migração
- **Backup simples:** Basta copiar o arquivo `db.sqlite3`
- **Restauração:** Substituir o arquivo existente pelo backup
- **Visualização:** Pode ser aberto com ferramentas como DB Browser for SQLite

### **Comandos úteis para SQLite:**
```bash
# Acessar o banco via Django shell
python manage.py dbshell

# Verificar estrutura das tabelas
python manage.py dbshell
> .tables                    # Lista todas as tabelas
> .schema nome_da_tabela     # Estrutura de uma tabela específica
> .quit                      # Sair do shell

# Fazer backup do banco
cp db.sqlite3 backup_db.sqlite3

# Restaurar backup
cp backup_db.sqlite3 db.sqlite3
```

---

## 🤖 Assistente com IA (Google Gemini)

### **Configuração e Integração:**
- **API:** `google.generativeai` com modelo `gemini-1.5-flash`
- **Segurança:** Chave API protegida via `python-dotenv`
- **Modelo:** Configuração automática via `settings.GEMINI_API_KEY`

### **⚠️ Configuração Obrigatória da API:**
Para utilizar o assistente de IA, é **obrigatório** criar o arquivo `.env` na raiz do projeto e adicionar sua chave da API do Google Gemini:

```env
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=sua-secret-key-django-aqui
DEBUG=True
```

### **Como obter a chave da API:**
1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada
5. Cole no arquivo `.env` substituindo `your_api_key_here`

### **Funcionalidades Avançadas:**
- **Prompt Educacional Personalizado:**
  - Sistema de prompts estruturados para respostas educativas
  - Explicações claras e práticas adaptadas ao nível do mentorado
  - Exemplos práticos e atividades sugeridas
  - Tom encorajador e motivacional
  - Limite de 200 palavras para respostas concisas

- **Validações e Segurança:**
  - Verificação de token do mentorado antes de processar
  - Validação de entrada (dúvida não pode estar vazia)
  - Tratamento robusto de erros com logging
  - Resposta estruturada em JSON com timestamp

- **Histórico Inteligente:**
  - Model `ConsultaIA` para salvar todas as consultas
  - Rastreamento de dúvidas e respostas por mentorado
  - Análise de progresso baseada em interações
  - Ordenação por data de criação (mais recente primeiro)

### **Configuração com python-dotenv:**
- **Carregamento automático** das variáveis de ambiente
- **Configuração segura** da API key do Google Gemini
- **Separação** entre configurações de desenvolvimento e produção

**Importância do dotenv:**
- **Segurança:** Mantém credenciais fora do código-fonte
- **Flexibilidade:** Diferentes configurações para dev/produção
- **Boas Práticas:** Evita exposição de APIs em repositórios
- **Funcionamento:** Essencial para o assistente IA funcionar

---

## ▶️ Como Executar o Projeto

### **1. Clonagem e Ambiente Virtual:**
```bash
git clone https://github.com/seu-usuario/mentorbook.git
cd mentorbook

# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### **2. Instalar Dependências:**
```bash
pip install -r requirements.txt
```

### **3. Configurar Variáveis de Ambiente:**
Crie o arquivo `.env` na raiz do projeto:
```env
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=sua-secret-key-django-aqui
DEBUG=True
```

> **⚠️ IMPORTANTE:** Sem o `GEMINI_API_KEY`, o assistente IA não funcionará!

### **4. Configurar Banco de Dados:**
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações (cria automaticamente o arquivo db.sqlite3)
python manage.py migrate

# (Opcional) Criar superusuário
python manage.py createsuperuser
```

### **5. Executar o Servidor:**
```bash
python manage.py runserver
```

### **6. Acessar a Aplicação:**
- **URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Cadastro de Mentor:** `/usuarios/cadastro/`
- **Login de Mentor:** `/usuarios/login/`
- **Acesso de Mentorado:** `/mentorados/auth/`

---

## 🔧 Comandos Úteis para Desenvolvimento

### **Banco de Dados:**
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Acessar shell do banco
python manage.py dbshell

# Resetar banco (cuidado!)
# 1. Deletar db.sqlite3
# 2. Deletar arquivos de migrations (exceto __init__.py)
# 3. Recriar migrações e aplicar
```

### **Debugging:**
```bash
# Shell interativo do Django
python manage.py shell

# Verificar estrutura das tabelas
python manage.py dbshell
> PRAGMA table_info(mentorados_mentorados);
> .quit
```

---

## 🔐 Segurança e Validações

### **Autenticação:**
- **Tokens únicos:** Gerados automaticamente com `secrets.token_urlsafe(8)`
- **Validação de unicidade:** Verificação antes de salvar no banco
- **Sessões Django:** Controle de acesso para mentores
- **Validação de propriedade:** Mentores só acessam seus dados

### **Proteções Implementadas:**
- **CSRF Protection:** Desabilitado apenas em endpoints AJAX seguros
- **HTTP Methods:** `@require_http_methods` para controle específico
- **Transações Atômicas:** `transaction.atomic()` para operações críticas
- **Validação de Entrada:** Tratamento de dados malformados
- **Controle de Acesso:** Verificação de permissões antes de operações
- **Geração Segura de Tokens:** Uso de `secrets` em vez de `random`

### **Exemplo de Validação:**
- **Validação de Token:** Verificação de existência e autenticidade do token
- **Geração de Token Único:** Loop para garantir unicidade no banco de dados
- **Verificação de Propriedade:** Mentores só acessam dados próprios
- **Validação de Entrada:** Tratamento de dados vazios ou malformados

---

## 🔧 Problemas Comuns

### **Erros de Configuração:**
- **Erro de API Key**: Verifique se o `GEMINI_API_KEY` está correto no arquivo `.env`
- **Arquivo .env não encontrado**: Certifique-se de criar o arquivo `.env` na raiz do projeto
- **Erro de migração**: Execute `python manage.py migrate --run-syncdb`

### **Problemas de Dependências:**
- **Erro de importação**: Verifique se todas as dependências foram instaladas com `pip install -r requirements.txt`
- **Versão do Python**: Certifique-se de usar Python 3.8+ 
- **Ambiente virtual**: Ative o ambiente virtual antes de instalar as dependências

### **Problemas de Mídia:**
- **Arquivos estáticos**: Execute `python manage.py collectstatic` se necessário
- **Upload de arquivos**: Verifique se a pasta `media/` tem permissões de escrita
- **Vídeos não carregam**: Verifique se o arquivo está no formato correto

---

## 📦 Dependências Principais

```txt
Django>=5.0.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
Pillow>=10.0.0
```

### **Funcionalidades Técnicas:**
- **Localização:** Configuração automática para português brasileiro
- **Formatação de Datas:** Conversão automática para formato local
- **Upload de Arquivos:** Gerenciamento seguro com exclusão física
- **Processamento de Imagens:** Pillow para manipulação de fotos
- **Logging:** Sistema de logs para debugging e monitoramento
- **Validação de Dados:** Verificação de integridade antes de salvar
- **Cálculo Automático:** Duração de reuniões e percentuais de progresso

---

## 🔮 Melhorias Futuras

- **Relatórios:** Exportação em PDF com dados de progresso
- **Notificações:** Sistema de e-mail e push notifications
- **Analytics:** Dashboard avançado com métricas detalhadas
- **Acessibilidade:** Implementação de padrões WCAG 2.1 AA
- **Modo Escuro:** Interface alternativa para melhor experiência
- **Histórico IA:** Busca e análise de consultas anteriores para mentores
- **API REST:** Endpoints para integração com aplicativos móveis
- **Backup Automático:** Sistema de backup e recuperação de dados
- **Calendário Integrado:** Visualização de reuniões em formato calendário
- **Notificações por WhatsApp:** Integração com API do WhatsApp Business
- **Relatórios de Progresso:** Análise detalhada do desempenho dos mentorados

---

## 🎯 Casos de Uso

### **Fluxo do Mentor:**
1. **Cadastro** → Login → Dashboard
2. **Criar Navigator** → Organizar mentorados
3. **Adicionar Mentorado** → Token gerado automaticamente
4. **Criar Tarefas** → Upload de vídeos educativos
5. **Definir Horários** → Disponibilidades de 50 minutos
6. **Acompanhar Reuniões** → Visualizar agendamentos
7. **Monitorar Progresso** → Ver consultas IA e estatísticas

### **Fluxo do Mentorado:**
1. **Acesso via Token** → Validação automática
2. **Visualizar Conteúdo** → Tarefas e vídeos
3. **Completar Tarefas** → Marcar como concluídas
4. **Assistir Vídeos** → Consumir conteúdo educativo
5. **Consultar IA** → Tirar dúvidas específicas
6. **Agendar Reunião** → Escolher categoria e horário
7. **Acompanhar Progresso** → Ver estatísticas e recomendações

---

## 🤝 Como Contribuir

### **Processo de Contribuição:**
1. Veja as [issues abertas](https://github.com/seu-usuario/mentorbook/issues)
2. Escolha uma issue ou proponha uma nova funcionalidade
3. Faça um fork do projeto
4. Criar branch para feature (`git checkout -b feature/nova-funcionalidade`)
5. Commit das mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
6. Push para branch (`git push origin feature/nova-funcionalidade`)
7. Abrir Pull Request

### **Padrões de Código:**
- **PEP 8:** Seguir padrões Python
- **Documentação:** Comentar código complexo
- **Testes:** Adicionar testes para novas funcionalidades
- **Segurança:** Validar todos os inputs de usuário

### **Tipos de Contribuição:**
- 🐛 **Bug fixes** - Correção de bugs
- ✨ **Features** - Novas funcionalidades
- 📚 **Documentação** - Melhorias na documentação
- 🎨 **UI/UX** - Melhorias na interface
- 🔧 **Refatoração** - Otimização de código

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Pedro Vinícius Rosário Rosário Rocha
