#Importa bibliotecas necessárias 
import random, sys

#Variáveis para controle de vitória, derrota e empate.
vitoria = 0
derrota = 0
empate = 0

#Menu de boas vindas
print("""-------------------------------
            PEDRA, PAPEL E TESOURA
      
Bem vindo ao jogo!
      
Escolha uma das opções abaixo:
      
      - Pedra (P)
      - Papel (A)
      - Tesoura (T)

No final terá a quantidade de vitórias, derrotas e empates.

Boa Sorte!

-------------------------------""")

while True: #Loop principal do jogo
    print("%s Vitórias, %s Derrotas, %s Empates" % (vitoria, derrota, empate))
    while True: #Loop da entrada do jogador
        print("Escolha entre: (P)pedra, (A)papel, (T)tesoura ou (S)sair.")
        jogador = input(">")
        if jogador == "S":
            print("Obrigado por jogar! Até a próxima.")
            sys.exit() #sai do programa
        if jogador == "P" or jogador == "A" or jogador == "T":
            break #Interrompe o loop da entrada do jogador
        print("Entrada inválida, escolha entre: (P)pedra, (A)papel, (T)tesoura ou (S)sair.")
    
    #Exibe a escolha do jogador
    if jogador == "P":
        print("PEDRA versus...")
    elif jogador == "A":
        print("PAPEL versus...")
    elif jogador == "T":
        print("TESOURA versus...")
    
    #Exibe a opção que o computador escolheu
    computador = random.randint(1, 3)
    if computador == 1:
        computador = "P"
        print("PEDRA")
    elif computador == 2:
        computador = "A"
        print("PAPEL")
    elif computador == 3:
        computador = "T"
        print("TESOURA")
    
    #Exibe o resultado do jogo
    if jogador == computador:
        print("Foi um empate!")
        empate = empate + 1
    elif jogador == "P" and computador == "T":
        print("Você venceu")
        vitoria = vitoria + 1 
    elif jogador == "A" and computador == "P":
        print("Você venceu!")
        vitoria = vitoria + 1
    elif jogador == "T" and computador == "A":
        print("Você venceu!")
        vitoria = vitoria + 1
    elif jogador == "P" and computador == "A":
        print("Você perdeu!")
        derrota = derrota + 1
    elif jogador == "A" and computador == "T":
        print("Você perdeu!")
        derrota = derrota + 1
    elif jogador == "T" and computador == "P":
        print("Você perdeu!")
        derrota = derrota + 1
    
              

