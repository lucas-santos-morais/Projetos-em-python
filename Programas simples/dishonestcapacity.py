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

