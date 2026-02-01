#Criando um DataFrame
#Importando bibliotecas necessárias.

# Biblioteca para manipulação de dados 
import numpy as np
import pandas as pd

df_temperatura = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

#Coluna criada com preenchimento dos valores nulos para trás
df_temperatura["preenchido_bill"] = df_temperatura["Temperatura"].bfill()

print(df_temperatura)