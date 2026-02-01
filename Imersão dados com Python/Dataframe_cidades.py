#Criando um DataFrame
#Importando bibliotecas necessárias.

# Biblioteca para manipulação de dados 
import numpy as np
import pandas as pd

df_cidades = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Calos", "Lucas", "Mariana"],
    "cidade": ["São Paulo", np.nan, "Belo Horizonte", np.nan, "Salvador"]
})

df_cidades["cidade_preenchida"] = df_cidades["cidade"].fillna("Não Informado")

print(df_cidades)

