import forca
import adivinhacao


def escolha_o_game():

    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
    print('●▬▬▬▬▬▬▬▬▬ஜ۩ Escolha um Game! ۩ஜ▬▬▬▬▬▬▬▬▬●')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')

    print('(1) Forca / (2) Adivinhação')

    jogo = int(input('Qual Jogo? '))

    if(jogo == 1):
        print('Jogando Forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando Adivinhação')
        adivinhacao.jogar()
    else:
        print('Jogo não Existe')


if(__name__ == '__main__'):
    escolha_o_game()
