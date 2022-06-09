from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

#CRIAÇÃO DO FORMULARIO 
class FormCadastrarFilmes(FlaskForm):
    nome = StringField(' Nome Do Filme', validators=[DataRequired()])
    sinopse = TextAreaField('Descrição', validators=[DataRequired()])
    link= StringField('Link de Download',validators=[DataRequired([])])
    botao_cadastrar = SubmitField('Cadastrar',validators=[DataRequired()]) 
    #