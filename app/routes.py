import json
from flask import jsonify, render_template, flash
from .process.arvore import teste
from app import app
import requests



@app.route('/')
@app.route('/index')
def index():                
    return render_template('base.html')


@app.route('/resultado/<dados>')
def resultado(dados): 
    dados = dados.split(",")
    verificacao = teste(dados) 
    return jsonify(verificacao)