from timeit import Timer
from flask import Flask, render_template, request, redirect, session, flash, url_for,send_from_directory
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from flask import Flask, render_template
from werkzeug.exceptions import abort
import MySQLdb.cursors
import mysql.connector
from datetime import datetime
from datetime import timedelta
#importa class banco
from conexaobanco import prepara_banco
#importa class 
from classweb import classjogo
#importa tela principal
from main import app
#import time
import time
import os
#importa class img
from classweb.classverificaimg import recupera_imagem
from classweb.classverificaimg import deleta_img
#varial pasta
from config import upload_img

app.secret_key="site"#segurança do banco
#mysql import
app.permanent_session_lifetime = timedelta(seconds=500)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'gamer'
mysql = MySQL(app)

@app.route('/novo')#inicio lista,v=erro,titulo="Jogos",lista=listajogos
def novo():
      #essa funçao verifica dados para logar na pagina
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM jogos')
    banco =cur.fetchall()
   
    return render_template('lista.html',titulo="Biblioteca Gamer",lista=banco)
@app.route('/buscar', methods=['POST', ])
def buscarjogo():

    buscar = request.form['buscar']
    print(buscar)
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"SELECT * FROM jogos where nome LIKE'%{buscar}%' ")
    #SELECT *FROM estoque WHERE codigo LIKE'%{self.descricao}%' or nome like '%{self.descricao}%
    banco =cur.fetchall()
    if buscar=='':
        return render_template('lista.html',titulo="Biblioteca Gamer",lista=banco)
    if buscar=="":
       return render_template('lista.html',titulo="Biblioteca Gamer",erro="background-color: red;color:white;",value="Campo Em branco")
    if not banco:
        flash("Produto Não Existe")
       
    return render_template('lista.html',titulo="Biblioteca Gamer",lista=banco)
@app.route('/ver/<int:id>')
def verjogos(id):
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"select * FROM jogos WHERE id = '{str(id)}'")
    banco =cur.fetchall()
    foto_img= recupera_imagem(id)#ess funçao sleecionar img e compara com id
    
    return render_template(
  'lista.html',editar=banco, foto=foto_img,mostra='display: block; background-color: #0a57a5;',
  prediction='model_prediction',
  show_predictions_modal=True

)

#add jogos  
@app.route('/lista', methods=['POST', ])
def addjogo():
    
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    arquivo = request.files['fotos']
    #essa funçao vai verifica se a nome cliente no banco
    verficanome=prepara_banco.Connection.pegainformçao(f"select nome FROM jogos  where nome='{nome}'")
    print(verficanome)
    if len(verficanome)!=0:
        flash("Nome  Ja existe")  
        return redirect(url_for('novo'))
    if nome=="" or categoria=="" or console=="":#verificar codigo e sua origem
        
        return redirect(url_for('novo'))
   
    else:  
        flash("Jogo Adicionado")  
        prepara_banco.Connection.adicionar("INSERT INTO  jogos (nome,catergoria,console)VALUES('{}','{}','{}')".format(nome,categoria,console)) 
        id=prepara_banco.Connection.pegainformçao("select id FROM jogos ORDER BY id DESC LIMIT 1")
        timestamp=time.time()#limpar memoria cache
        
        arquivo.save(f'{upload_img}/{id[0][0]}-{timestamp}.png')
        return redirect(url_for('novo'))  
@app.route('/editar/<int:id>')#ESSA 
def editar(id):
    
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"select * FROM jogos WHERE id = '{str(id)}'")
    banco =cur.fetchall()
    foto_img= recupera_imagem(id)#ess funçao sleecionar img e compara com id

    return render_template('alterajogo.html',editar=banco, foto=foto_img )
    ##ados2=prepara_banco.Connection.pegainformçao(f"select FROM jogos WHERE id='{str(id)}' ")
@app.route('/atualizar', methods=['POST', ])#ESSA FUNÇAO PEGA ID DO ITEM QUE FOI SELECIONADO DA TABELA E ALTERA OS DADOSDO ITEN
def atualizar():
    id = request.form['id']  
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"update jogos set nome='{nome}',catergoria='{categoria}',console='{console}' where id='{id}'")

    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM jogos')
    banco =cur.fetchall()
    arquivo = request.files['fotos']
    
    timestamp=time.time()#limpar memoria cache
    deleta_img(id)#DELETA FOTO ANTERIO
    
    arquivo.save(f'{upload_img}/{id}-{timestamp}.png')
    return render_template('lista.html',titulo="Biblioteca Gamer",lista=banco)
 
#excluir jogos
@app.route("/excluir/<int:id>",methods=['GET', 'POST'])
def excluir(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    funcionarios=prepara_banco.Connection.apaga(f"DELETE FROM jogos WHERE id = {str(id)}")
    deleta_img(id)#verifica se foto existe com mesmo id e apagar
    flash("Jogo Apagado Com sucesso")  
    return redirect(url_for("reflesk",lista=funcionarios))
    
@app.route('/novo')
def reflesk():
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM jogos')
    banco =cur.fetchall()  
    return redirect(url_for('novo',erro=banco))


@app.route(f'/uploads/<nome_arquivo>')#essa funçao selecionar img da pasta referente id
def image(nome_arquivo):
    print(nome_arquivo)
    return send_from_directory('uploads', nome_arquivo)

