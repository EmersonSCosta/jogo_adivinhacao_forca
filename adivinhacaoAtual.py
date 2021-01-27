import random

print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Emerson Game ۩ஜ▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')


numero_secreto = random.randrange(1, 51)
total_de_tentativas = 0
rodadas = 1
pontos = 1000
desconto = numero_secreto

print('Qual nivel de dificuldade ?')
print('facil (F), medio (M), dificil (D)')
nivel = input('Digite um nivel: ')

if(nivel == 'F'):
    total_de_tentativas = 15
elif(nivel == 'M'):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

print(f'Sua Pontuação Atual: {pontos}')

for rodadas in range(1, total_de_tentativas + 1):

    print(f'Tentativa {rodadas} de {total_de_tentativas}')
    chute_str = input('Digite um número entre 1 e 50: ')
    print('Você digitou ', chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 50):
        print('Você não digitou um número entre 1 e 50')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Parabéns! Você acertou!')
        pontos = pontos + 1000
        print(f'Pontuação Atual: {pontos}')
        break
    else:
        if(maior):
            pontos = pontos - chute
            desconto = desconto / 100
            pontos = abs and int(pontos * desconto)
            print('O seu chute foi maior do que o número secreto!', end='\n')
            print(f'Pontuação Atual: {pontos}')
        elif(menor):
            pontos = pontos - chute
            desconto = desconto / 100
            pontos = abs and int(pontos * desconto)
            print('O seu chute foi menor do que o número secreto!', end='\n')
            print(f'Pontuação Atual: {pontos}')

print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Fim do Game ۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
