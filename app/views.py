from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/usuarios')
def usuarios():
    return render_template('segunda_pagina.html')

@app.route('/editar')
def editar():
    return render_template('editar.html')


