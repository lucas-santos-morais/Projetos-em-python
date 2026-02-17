#importando a biblioteca Tkinter para criar uma interface gráfica
import tkinter as tk 
from tkinter import Label, Frame


#Criando a janela principal da aplicação
grade = tk.Tk()

#Defini o tamanho da janela
grade.geometry("550x400")

#Criando um titulo para a janela
grade.title("Caculadora de Capacidade de Armazenamento")

# Calcula a diferença entre as capacidades anunciadas e reais
def calcular_diferenca():
    if unidade.get() =="TB" or unidade.get() == "tb":
        discrepancia = 1000000000000 / 1099511627776
        real_capacidade = (round(float(capacidade.get()) * discrepancia,2))
        resultado["text"] = f"A capacidade do seu armazenamento é {real_capacidade} {unidade.get()}"
    elif unidade.get() =="GB" or unidade.get() == "gb":
        discrepancia = 1000000000 / 1073741824
        real_capacidade = (round(float(capacidade.get()) * discrepancia,2))
        resultado["text"] = f"A capacidade do seu armazenamento é {real_capacidade} {unidade.get()}"
    else:
        resultado["text"] = "unidade inválida. Use TB ou GB."

#Criando um frame para organizar os elementos dentro da janela
frame = Frame(grade, padx=30, pady=10)
frame.grid(column=0, row=0)

#Titulo da calculadora
tk.Label(
    frame,
    text="Calculadora de armazenamento",
    font=("Arial",15, "bold"),
    pady=20,
    justify="center"
).grid(column=0, row=0, padx=10, columnspan=2)

#Criando um label para exibir as instruções para o usuário
tk.Label(
    frame,
    text="Digite se seu armazenamento é TB ou GB e digite a capacidade.",
    font=("Arial",11),
    pady=40,
    wraplength=400,   # largura máxima antes de quebrar linha
    justify="center"    # alinhamento do texto
).grid(column=0, row=1, padx=5)



#Criando um label para exibir legendas para as siglas TB e GB
tk.Label(
    frame,
    text="TB = Terabyte \n GB = Gigabyte",
    font=("Arial",11),
    justify="right"
).grid(column=1, row=1, padx=5)


#Criando um label para solicitar as siglas TB ou GB e um campo para entrada de dados
tk.Label(
    frame,
    text="TB ou GB:",
    font=("Arial",11),
    pady=20,
    justify="left"
).grid(column=0, row=2, padx=20)

unidade=tk.Entry(frame)
unidade.grid(column=1, row=2)


#Criando um label para solicitar a capacidade do armazenamento e um campo para entrada de dados
tk.Label(
    frame,
    text="Capacidade:",
    font=("Arial",11),
    pady=20,
    justify="left"
).grid(column=0, row=3)

capacidade=tk.Entry(frame)
capacidade.grid(column=1, row=3)

#Criando um botão para calcular a capacidade real do armazenamento
tk.Button(
    frame,
    text="Calcular",
    font=("Arial",10),
    width=10,
    height=1,
    command=calcular_diferenca
).grid(column=0, row=4, columnspan=2)


#Criando um label para exibir o resultado do cálculo
resultado = tk.Label(
    frame,
    font=("Arial",10),
    pady=20,
    justify="center"
)
resultado.grid(column=0, row=5, columnspan=2)


#Roda o programa
grade.mainloop()



'''
print("Digite se seu armazenamento é TB ou GB, use apenas essas siglas")
unidade = input(">")

# Calcula a diferença entre as capacidades anunciadas e reais
if unidade =="TB" or unidade == "tb":
    discrepancia = 1000000000000 / 1099511627776
elif unidade =="GB" or unidade == "gb":
    discrepancia = 1000000000 / 1073741824
else:
    print("unidade inválida. Use TB ou GB.")


print("Entre com a capacidade do seu armazenamento:")
capacidade = float(input(">"))

# Calcula a capacidade real, arredondando para duas casas decimais
real_capacidade = (round(capacidade * discrepancia,2))

print(f"A capacidade do seu armazenamento é {real_capacidade} {unidade}")
'''
