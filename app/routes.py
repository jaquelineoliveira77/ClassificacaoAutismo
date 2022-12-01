import json
from flask import jsonify, render_template, flash, request
from .process.arvore import teste
from app import app
import requests




@app.route('/')
@app.route('/index')
def index():                
    return render_template('base.html')

@app.route('/exemplo') # rota apenas de exemplo
def exemplo(): 
    dados = "842302,M,17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189"
    response = requests.get("http://127.0.0.1:5000/resultado/" + dados)
    resposta = response.json()
    return jsonify(resposta)

@app.route('/resultado/<dados>')# recebe dados anexados na rota, no momento recebe uma string e separa elementos por vírgula, formatação pode ser modificada depois
def resultado(dados): 
    dados = dados.split(",")
    verificacao = teste(dados) 
    return jsonify(verificacao)

# Exemplo utilizando formatação do form, eu usei letras do alfabeto como argumentos mas no form seriam o name de cada campo 
@app.route('/exemploForms')
def exemplo(): 
    dados = "a=842302&b=M&c=17.99&d=10.38&e=122.8&f=1001&g=0.1184&h=0.2776&i=0.3001&j=0.1471&k=0.2419&l=0.07871&m=1.095&n=0.9053&o=8.589&p=153.4&q=0.006399&r=0.04904&s=0.05373&t=0.01587&u=0.03003&v=0.006193&w=25.38&x=17.33&y=184.6&z=2019&aa=0.1622&bb=0.6656&cc=0.7119&dd=0.2654&ee=0.4601&ff=0.1189"
    response = requests.get("http://127.0.0.1:5000/resultadoForms?" + dados)
    resposta = response.json()
    return jsonify(resposta)


# É para funcionar com form, a orderm dos dados precisa ser a mesma que do arquivo csv usado para criar a árvore
@app.route('/resultadoForms')
def resultado(): 
    dados = request.args.values()
    verificacao = teste(dados) 
    return jsonify(verificacao)
