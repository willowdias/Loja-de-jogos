#importa tela principal
from main import app
from flask import Flask
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from classviews import*
from config import*
#pagina login 
@app.route('/login')
def login():#TELA INICIAL LOGIN
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)
#logar na pagina lista
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    login=request.form["usuario"]
    senha=request.form['senha']
    dados2=prepara_banco.Connection.pegalogin(f"SELECT *FROM tb_usuario where  login_='{login}' and senhar='{senha}' ")  
    if dados2:
        session["usuario_logado"]=request.form["usuario"]
        flash(session["usuario_logado"]+(' Usuario logado'))
       
        return redirect(url_for('novo'))
    else:
        flash("usuario incorreto")
        return redirect(url_for('login'))    
#reloga pra login
@app.route('/logout', methods=['POST', ])  
def logoute():
    session["Usuario logado"] = None
    flash("Usuario Foi Deslogado")
    return redirect(url_for('login'))