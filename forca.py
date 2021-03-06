def jogar():
    import random
    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Forca ۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
    arquivo = open('BD/palavras.txt', 'r')
    lista_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero].upper()
    letra_acertou = ['_' for x in palavra_secreta]
    enforcou = False
    acertou = False
    palavras_erradas = 0
    print(letra_acertou)
    while(not enforcou and not acertou):
        chute = input('Qual a letra? ')
        chute = chute.strip().upper()
        if(len(chute) < 2):
            if(chute in palavra_secreta):
                posicao = 0
                for x in palavra_secreta:
                    if(chute == x):
                        letra_acertou[posicao] = x
                    posicao += 1
            else:
                palavras_erradas += 1
            enforcou = palavras_erradas == 6
            acertou = '_' not in letra_acertou
            if(acertou == True):
                print('Você Ganhou!!!')
            print(letra_acertou)
            print(f'Errou {palavras_erradas}')
        else:
            print('Digitou mais de uma letra')
            continue
    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n●▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Fim do Game ۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')


if(__name__ == '__main__'):
    jogar()
