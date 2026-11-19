```markdown
# 🚀 NexusUsers

> Aplicação web full-stack para gerenciamento e administração eficiente de usuários, construída com Python, Flask e SQLite.

O **NexusUsers** centraliza operações essenciais de **CRUD** (cadastro, visualização, edição e remoção de usuários) em uma estrutura modular e limpa, combinada com uma interface moderna em **Dark Mode** com efeitos de *glassmorphism* e layout responsivo.

---

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python 3, Flask
* **Banco de Dados & ORM:** SQLite3, Flask-SQLAlchemy
* **Front-end:** HTML5, CSS3 (CSS Grid, Flexbox, Linear Gradients, Glassmorphism), Jinja2

---

## 📁 Arquitetura do Projeto

```text
NexusUsers/
├── app/
│   ├── __init__.py          # Inicialização da instância do Flask e carregamento das rotas
│   ├── views.py             # Gerenciador de rotas e fluxo de renderização
│   ├── static/              # Folhas de estilo (paleta dark clean e gradientes de 90°)
│   └── templates/           # Interfaces HTML dinâmicas
│       ├── index.html           # Página principal com formulário de cadastro
│       ├── segunda_pagina.html  # Página de listagem de usuários
│       └── editar.html          # Interface para editar, salvar e excluir usuários
├── main.py                  # Ponto de entrada da aplicação (modo debug ativado)
└── README.md

```

---

## 🎨 Interface e Estilização

* **Estética Dark Mode Clean:** Fundo em tons de grafite escuro com transições suaves (`linear-gradient(90deg)`) e contrastes equilibrados para leitura confortável.
* **Componente `.HeaderNexus`:** Estruturado com **CSS Grid** (`grid-template-columns`), alinhamento centralizado, margens automáticas e espaçamento (`gap`) entre logo e navegação.
* **Alinhamento de Ações:** Botões organizados em linha via Flexbox/Grid com espaçamentos consistentes.

---

## 🔌 Rotas e Endpoints

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` / `POST` | `/` | Renderiza a página inicial com o formulário de cadastro e navegação interna. |
| `GET` / `POST` | `/usuarios` | Registra novos usuários no banco de dados e exibe a listagem. |
| `GET` | `/editar` | Lista os usuários cadastrados com opção de seleção para edição. |
| `GET` / `POST` | `/editar_usuario/<int:ID>` | Carrega os dados do usuário pelo `ID`, atualiza as informações ou remove o registro no banco. |

---

## 🗄️ Estrutura do Banco de Dados

O sistema utiliza **SQLite3** integrado via **SQLAlchemy**, composto pela tabela `usuarios`:

| Coluna | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| `ID` | `Integer` | `PRIMARY KEY` | Identificador único do usuário |
| `nome` | `String` | `NOT NULL` | Nome completo do usuário |
| `email` | `String` | `NOT NULL` | Endereço de e-mail |
| `telefone` | `String` | `NOT NULL` | Número de telefone/contato |

---

## ⚙️ Como Executar Localmente

1. **Clone o repositório:**
```bash
git clone [https://github.com/Carl1nx/NexusUsers.git](https://github.com/Carl1nx/NexusUsers.git)
cd NexusUsers

```


2. **Crie e ative um ambiente virtual:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

```


3. **Instale as dependências:**
```bash
pip install flask flask-sqlalchemy

```


4. **Execute a aplicação:**
```bash
python main.py

```


5. **Acesse no navegador:**
```text
[http://127.0.0.1:5000](http://127.0.0.1:5000)

```



```

*(Nota: Como o Markdown acima possui blocos de código aninhados para a árvore de pastas e comandos de terminal, a visualização da plataforma pode quebrar a caixa única de cópia. Se quiser o texto puro sem renderização para selecionar tudo com `Ctrl+A` / `Ctrl+C`, me avise que envio dentro de um bloco simples de texto!)*

```
