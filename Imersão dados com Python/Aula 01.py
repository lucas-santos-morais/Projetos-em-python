#Importando a biblioteca e dando um apelido
import pandas as pd

#Importando base de dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

#Variáveis do ambiente

linhas, colunas = df.shape[0], df.shape[1]


#Imprimi no terminal as 10 primeiras linhas
print(df.head(10))

#imprimi as informações da base de dasdos
print(df.info())

#Imrimi as estatísticas descritivas da base de dados
print(df.describe())

#Imprimi o número de linhas e colunas da base de dados
print("Linhas:", linhas)
print("colunas:", colunas)

#Imprimi o nome das colunas da base de dados
print(df.columns)

#Criando uma variável para renomear as colunas
renomear_colunas = {
    "work_year": "ano_de_trabalho",
    "experience_level": "nivel_de_experiencia",
    "employment_type": "tipo_de_contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda_do_salario",
    "salary_in_usd": "salario_em_usd",
    "employee_residence": "residencia_do_funcionario",
    "remote_ratio": "percentual_trabalho_remoto",
    "company_location": "localizacao_da_empresa",
    "company_size": "porte_da_empresa"
}

#Exibi as colunas renomeadas
df.rename(columns=renomear_colunas, inplace=True)
print(df.columns)

#Exibi os valores da coluna
print(df["nivel_de_experiencia"].value_counts())

print(df["tipo_de_contrato"].value_counts())

#Renomear os nomes da categoria da coluna nivel de experiencia
experiencia = {
    "SE": "Senior",
    "MI": "Pleno",
    "EN": "Junior",
    "EX": "Executivo"
}

df["nivel_de_experiencia"].replace(experiencia, inplace=True)
print(df["nivel_de_experiencia"].value_counts())



