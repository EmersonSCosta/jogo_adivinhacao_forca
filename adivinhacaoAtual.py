import random

print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Emerson Game ۩ஜ▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')


numero_secreto = random.randrange(1, 51)
total_de_tentativas = 6
rodadas = 1


for rodadas in range(1, total_de_tentativas + 1):

    print(f"Tentativa {rodadas} de {total_de_tentativas}")
    chute_str = input("Digite um número entre 1 e 50: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 50):
        print("Você não digitou um número entre 1 e 50")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!", end='\n')
            print("")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!", end='\n')
            print("")

print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Fim do Game ۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
