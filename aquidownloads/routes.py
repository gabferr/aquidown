from aquidownloads import app,database
from aquidownloads.forms import FormCadastrarFilmes
from aquidownloads.models import Cadastrar
from flask import request,flash,render_template

#FUNCÃO PRINCIPAL QUE RENDERIZA A PAGINA PRINCIPAL
@app.route("/")
def hello_world():
    return render_template ('home.html')
#

#FUNCAO QUE RENDERIZA A PAGINA PARA CADASTRAR OS FILMES
@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar_filmes():
    form_cadastrar = FormCadastrarFilmes()

    if form_cadastrar.validate_on_submit() and 'botao_cadastrar' in request.form:
        # O FORMULARIO CADASTRAR É PASSADO PARA UMA VARIAVEL
        cadastrar = Cadastrar(nome=form_cadastrar.nome.data,sinopse=form_cadastrar.sinopse.data,link=form_cadastrar.link.data)
        #ESSE COMANDO FAZ UMA PRÉ CONFIRMAÇÃO DAS INFORMAÇÕES DIGITADAS NO FORMULÁRIO E É PASSADO A VARIAVEL cadastrar COMO PARAMETRO
        database.session.add(cadastrar)
        #COMANDO COMMIT CONFIRMA A GRAVAÇÃO DAS INFORMAÇÕES NO BANCO DE DADOS
        database.session.commit()
        flash('Filme cadastrado com sucesso', 'alert-success' )
    return render_template ('cadastrar_filmes.html',form_cadastrar=form_cadastrar)
#ESSA FUNÇÃO ESTÁ RETORNANDO A PAGINA DE CADASTRO E O FORMULARIO INSTANCIADO NA PRIMEIRA  LINHA E RETORNA 
#O FORMULARIO COMO UMA VARIAVEL E SENDO ACESSADO PELO HTML
