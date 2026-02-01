#Para rodar o código, retire os comentários das linhas do print abaixo.

#Importando a biblioteca e dando um apelido
import pandas as pd

#Importando base de dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

#Verificando dados faltantes na base de dados
#print(df.isnull().sum())

#Exibindo os anos únicos da coluna "work_year"
#print(df["work_year"].unique())

#Exibindo as linhas com dados faltantes
#print(df[df.isnull().any(axis=1)])






