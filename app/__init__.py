import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define o caminho absoluto da pasta raiz do projeto
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

app = Flask(__name__)
# Configura o banco para ser criado diretamente na raiz do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Nexus.db')

db = SQLAlchemy()
db.init_app(app)

from app import views