import json
from flask import jsonify, render_template, flash
from .process.arvore import teste
from app import app
import requests



@app.route('/')
@app.route('/index')
def index():                
    return render_template('base.html')

@app.route('/exemplo')
def exemplo(): 
    dados = "842302,M,17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189"
    response = requests.get("http://127.0.0.1:5000/resultado/" + dados)
    resposta = response.json()
    return jsonify(resposta)

@app.route('/resultado/<dados>')
def resultado(dados): 
    dados = dados.split(",")
    verificacao = teste(dados) 
    return jsonify(verificacao)