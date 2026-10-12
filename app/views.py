from app import app, db
from flask import render_template, url_for, redirect, request

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(100), nullable=False)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nome_form = request.form.get('nomeForm')
        email_form = request.form.get('emailForm')
        telefone_form = request.form.get('telefoneForm')

        novo_usuario = Usuario(nome=nome_form, email=email_form, telefone=telefone_form)
        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for('usuarios'))

    return render_template('segunda_pagina.html')


# 1. Rota para listar os utilizadores na página de edição
@app.route('/editar')
def editar():
    # Busca todos os utilizadores guardados na base de dados
    lista_usuarios = Usuario.query.all()
    # Passa a lista para o template 'editar.html' através da variável 'usuarios'
    return render_template('editar.html', usuarios=lista_usuarios)


# 2. Rota para carregar o formulário de edição de um utilizador específico (por ID)
@app.route('/editar_usuario/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    # Procura o utilizador pelo ID ou retorna erro 404 se não existir
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        # Atualiza os dados com o que vier do formulário de edição
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        usuario.telefone = request.form.get('telefone')

        db.session.commit()
        return redirect(url_for('editar'))

    # Se for GET, renderiza um formulário pré-preenchido com os dados atuais
    return render_template('formulario_editar.html', usuario=usuario)