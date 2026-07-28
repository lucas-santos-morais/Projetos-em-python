import pandas as pd
import qrcode
import os

# =========================
# LER PLANILHA
# =========================

df = pd.read_excel("Sistema_Presenca_Idosos.xlsx")

print(df[["ID", "Nome", "Link"]].head())

# =========================
# CRIAR PASTA DOS QRCODES
# =========================

os.makedirs("qrcodes", exist_ok=True)

# =========================
# GERAR QRCODES
# =========================

for index, row in df.iterrows():

    idoso_id = row["ID"]
    nome = row["Nome"]
    link = row["Link"]

    # Criar QR Code
    qr = qrcode.make(link)

    # Nome do arquivo
    nome_limpo = str(nome).replace(" ", "_")
    nome_arquivo = f"{idoso_id}_{nome_limpo}.png"

    # Caminho final
    caminho = os.path.join("qrcodes", nome_arquivo)

    # Salvar imagem
    qr.save(caminho)

    print(f"QR Code gerado: {nome_arquivo}")

print("\nTodos os QR Codes foram gerados!")


