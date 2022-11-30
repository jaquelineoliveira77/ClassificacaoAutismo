import pandas as pd
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import sklearn.metrics




dados = pd.read_csv('data.csv')
dados.drop(['id', 'Unnamed: 32'], axis = 1, inplace = True)
le = LabelEncoder()
dados['diagnosis']=le.fit_transform(dados['diagnosis'])
print("Quantidade de colunas: ",dados.shape[1])
dados.head(10)





corr_matrix = dados.corr().abs() 
mask = np.triu(np.ones_like(corr_matrix, dtype = bool))
tri_df = corr_matrix.mask(mask)
to_drop = [x for x in tri_df.columns if any(tri_df[x] > 0.92)]
dados2 = dados.drop(to_drop, axis = 1)
print("Quantidade de colunas do dataframe original: ",dados.shape[1])
print("Quantidade de colunas do dataframe reduzido: ",dados2.shape[1])







X = dados2.drop(["diagnosis"] ,axis="columns")
y = dados2['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=True)
modelo = linear_model.LogisticRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
a = modelo.coef_
b =  modelo.intercept_
print("Coeficientes da reta: \n")
print("a = ",a)
print("b = ",b)
acc = accuracy_score(y_test, y_pred)
print("Acurácia: ", acc)
matriz = confusion_matrix(y_test, y_pred)
print(matriz)
relatorio = classification_report(y_test, y_pred)
print(relatorio)






X = dados2.drop(["diagnosis"] ,axis="columns")
y = dados2['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=True)
modelo = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Acurácia: ", acc)
matriz = confusion_matrix(y_test, y_pred)
print(matriz)
relatorio = classification_report(y_test, y_pred)
print(relatorio)




X = dados2.drop(["diagnosis"] ,axis="columns")
y = dados2['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=True)
modelo = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=0)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Acurácia: ", acc)
matriz = confusion_matrix(y_test, y_pred)
print(matriz)
relatorio = classification_report(y_test, y_pred)
print(relatorio)



X = dados2.drop(["diagnosis"] ,axis="columns")
y = dados2['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=True)
modelo = DecisionTreeClassifier(criterion='entropy', max_depth=10, random_state=0)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Acurácia: ", acc)
matriz = confusion_matrix(y_test, y_pred)
print(matriz)
relatorio = classification_report(y_test, y_pred)
print(relatorio)

def teste(dados):
    with open('example.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(X_test) # cabeçalho
        writer.writerow(dados) # dados
    arquivo = pd.read_csv('example.csv')
    lista_numpy = modelo.predict(arquivo)
    lista_resultado = lista_numpy.tolist()
    match lista_resultado[0]:
        case 0:
            resposta = 'negativo'
        case 1:
            resposta = 'positivo'
        case default:
            resposta = 'erro'
    
    return resposta