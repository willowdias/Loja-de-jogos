
import os
from unicodedata import category
from flask_wtf import Flaskform
from wtforms import StringField,validators

class Formulario_verificar(Flaskform):
    nome=StringField('Nomo Do jogo',[validators.DataRequired(),validators.Length()])
    categoria=StringField()
    console=StringField()