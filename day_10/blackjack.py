from random import randint


def play():
    dealer = []
    player = []
    baralho = ['a', '2', '3', '4', '5', '6',
               '7', '8', '9', '10', 'j', 'q', 'k'] * 4

    # Um turno
    for _ in range(2):
        c1 = baralho.pop(randint(0, len(baralho)))
        dealer.append(c1)
        c2 = baralho.pop(randint(0, len(baralho)))
        player.append(c2)
    # Exibe uma carta do dealer e as cartas do player
    print(dealer[0], "?")
    print(player)

    # Enquanto mao do player valer menos que 21 ofereço a opçao de baixar ou parar

    # Criar logica para os As

    # se mao do player for 21 os players mostram as maos

    # Se mao do player for maior que 21 o dealer leva a rodada

    # Dealer vai puxar enquanto tiver 17 ou menos de resultado

    # Compara os valores


if __name__ == '__main__':
    play()
