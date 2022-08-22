from multiprocessing import connection
import string
import mysql.connector
from datetime import datetime
from flask_bcrypt import Bcrypt
class Connection():
    def __init__(self):
        pass    
    def connect(self):
        
        
        try:
            
            self.banco = mysql.connector.connect(
                    
                host='127.0.0.1',
                user="root",
                password=''
                    
                )  

            if self.banco.is_connected():
                print("banco connectador")
                cursor = self.banco.cursor()
                cursor.execute(" CREATE DATABASE IF NOT EXISTS Gamer") 
                
            
            else:
                print('Connection Failed')  
        except:
            print("Banco Dados Nao Encontrado")
    def createtabela():
        
       
        mydb = mysql.connector.connect(
        host=f"127.0.0.1",
        user=f"root",
        passwd=f"",
        database=f"gamer",
        )

        mycursor = mydb.cursor()
        #cadastro de usuario
        mycursor.execute("""CREATE TABLE IF NOT EXISTS jogos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(80),catergoria varchar(80),console varchar(80) )""")
        
        #cadastro de usuario
        mycursor.execute("""CREATE TABLE IF NOT EXISTS tb_usuario (
        id INT AUTO_INCREMENT PRIMARY KEY,
        login_ VARCHAR(80),senhar varchar(80),senha_verificar varchar(80),data_cadastro varchar(50),data_emissao varchar(50),horario_cadastro varchar(25),status varchar(50) )""")
        #inserir cadastro usuario
        mycursor.execute(f"SELECT * FROM tb_usuario " )
        ver=mycursor.fetchall()
        if not ver:#essa funçao verifica se usuario existe
            horario=datetime.today().strftime('%H:%M')
            data=datetime.today().strftime('%d/%m/%Y')
            data_atual=datetime.today().strftime('%d/%m/%Y')
            login="sistema"
            
            senha="1"
            statos="Administrador"
            query = """INSERT INTO tb_usuario(login_,senhar,senha_verificar,data_cadastro,data_emissao,horario_cadastro,status) values(%s,%s,%s,%s,%s,%s,%s)"""
            mycursor.execute(query, (login,senha,senha,data,data_atual,horario,statos))  
    def pegalogin(sql):
       
        mydb = mysql.connector.connect(
        host=f"127.0.0.1",
        user=f"root",
        passwd=f"",
        database=f"gamer",
        )

        mycursor = mydb.cursor()
        mycursor.execute(f"{sql}")
        return mycursor.fetchone()
    def pegainformçao(sql):
        mydb = mysql.connector.connect(
        host=f"127.0.0.1",
        user=f"root",
        passwd=f"",
        database=f"gamer",
        )

        mycursor = mydb.cursor()
        mycursor.execute(f"{sql} " )
        return mycursor.fetchall()
    def adicionar(sql):#acicionar item
        mydb = mysql.connector.connect(
        host=f"127.0.0.1",
        user=f"root",
        passwd=f"",
        database=f"gamer",
        )

        cursor=mydb.cursor()
        cursor.execute(sql)  
        mydb.commit() 
    def apaga(sql):
        mydb = mysql.connector.connect(
        host=f"127.0.0.1",
        user=f"root",
        passwd=f"",
        database=f"gamer",
        )

        mycursor = mydb.cursor()
        mycursor.execute(f"{sql} ")
        mydb.commit() 
        mydb.close()
Connection().connect()
Connection.createtabela()