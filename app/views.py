from app import app
from app.models import db, Usuario
from flask import render_template, url_for, redirect, request

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



@app.route('/editar')
def editar():
    lista_usuarios = Usuario.query.all()
    return render_template('editar.html', usuarios=lista_usuarios)



@app.route('/editar_usuario/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        usuario.telefone = request.form.get('telefone')

        db.session.commit()
        return redirect(url_for('editar'))


    return render_template('formulario_editar.html', usuario=usuario)