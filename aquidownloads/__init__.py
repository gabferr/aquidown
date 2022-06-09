from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CRIA CHAVE SECRETA PARA COLOCAR NO FORMULARIO DENTRO DO HTML
app.config['SECRET_KEY'] = '85bfb1d10b5c624add777301e572f4a5'
#

#CONFIGURAÇÃO DA CONEXÃO DO BANCO DE DADOS COM O SISTEMA
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmes.db'
database = SQLAlchemy(app)
#

from aquidownloads import routes
