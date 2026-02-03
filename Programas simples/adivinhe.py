#Jogo de advinhar o número 

import random
numero_secreto = random.randint(1, 20)

print("""-------------------------------
                ADVINHE O NÚMERO
       
Bem vindo ao jogo de advinhar o número!
      
Escolha um número entre 1 á 20.
      
Regras:

      - Você tem  6 chances para advinhar.
      - A cada tentativa, o programa irá dizer se está próximo ou longe do número secreto.

Digite seu palpite abaixo
    
Boa sorte!

-------------------------------            
""")

#Solicita que o jogador tente adivinhar o número 6 vezes

for tentativas in range(1, 7):
    print("Tente adivinhar")
    tentativas = int(input(">"))

    if tentativas < numero_secreto:
        print("Seu palpite foi baixo.")
    elif tentativas > numero_secreto:
        print("Seu palpite foi alto.")
    else:
        break #Esta condição é verdadeira se o jogador advinhou o número

if tentativas ==numero_secreto:
    print("Parabéns! Você acertou o número secreto " + str(tentativas) + " tentativas.")
else:
    print("Que pena! O número secreto era" + str(numero_secreto))

    

