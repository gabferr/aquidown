from aquidownloads import database
from datetime import datetime

#CRIAÇÃO DA TABELA DO BANCO DE DADOS
class Cadastrar(database.Model):
    id= database.Column(database.Integer,primary_key=True)
    nome=database.Column(database.String,nullable=False)
    sinopse=database.Column(database.Text,nullable=False)
    link=database.Column(database.String,nullable=False)
    foto=database.Column(database.String,default='default.jpg',nullable=False)
    data_criacao= database.Column(database.DateTime, nullable=False,default=datetime.utcnow())
    #