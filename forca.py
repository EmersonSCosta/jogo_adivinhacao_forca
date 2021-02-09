def jogar():

    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Forca ۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')

    palavra_secreta = 'banana'

    letra_acertou = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False

    print(letra_acertou)

    while(not enforcou and not acertou):

        chute = input('Qual a letra? ')
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                #print(f'Encontrei a Letra [{letra}] na posição [{posicao}]')
                letra_acertou[posicao] = letra
            posicao = posicao + 1

        print(letra_acertou)

    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
    print('●▬▬▬▬▬▬▬▬▬▬▬ஜ۩ Fim do Game ۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')


if(__name__ == '__main__'):
    jogar()
