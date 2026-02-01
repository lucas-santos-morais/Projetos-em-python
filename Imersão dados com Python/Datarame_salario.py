#Criando um DataFrame
#Importando bibliotecas necessárias.

# Biblioteca para manipulação de dados 
import numpy as np
import pandas as pd

#Coluna criada com nome e salario com valores 
df_salarios = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Calos", "Lucas", "Mariana"],
    "salario":[4500, np.nan, 5000, np.nan, 6000]
})

#Coluna criada com média salarial, preenche os valores nulos com a média e arredonda as casas decimais
df_salarios["salario_media"] = df_salarios["salario"].fillna(df_salarios["salario"].mean().round(2))

#Coluna criada com mediana salarial, preenche os valores nulos com a mediana
df_salarios["salario_mediana"] = df_salarios["salario"].fillna(df_salarios["salario"].median())

#Exibe o DataFrame com as novas colunas
print(df_salarios)
