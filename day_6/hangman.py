from random import choice
from hangman_art import stages, logo
from palavras import palavras_aleatorias as p



def play():
    # Gerando área de input do usuario
    entradas = []

    # Quantidade de vidas restantes
    vidas = len(stages)

    # Escolhendo a palavra secreta
    palavra_secreta = choice(p)

    # Letras escolhidas pelo usuario
    letras = set()

    # Loop principal do jogo
    # TODO criar sistema de vitória caso o jogar acerte a palavra
    while True:
        letra = input("Digite uma letra: ").lower()
        letras.add(letra)
        if letra not in palavra_secreta:
            vidas = reduzir_vida(vidas)
            print(vidas)
            mostrar_erro(vidas, letra)
            if vidas == 0:
                fim_de_jogo()
                return
        exibir_tentativa(letras, palavra_secreta)


def exibir_tentativa(tentativas:set[str], palavra):
    entradas = ["_" if letra not in tentativas else letra for letra in palavra]
    print("".join(entradas))


def reduzir_vida(vidas):
    return vidas - 1


def mostrar_erro(vidas: int, letra: str):
    print(vidas)
    print(stages[vidas])
    print(f"A letra \"{letra}\" não está na palavra")
    print()


def fim_de_jogo(palavra: str):
    print("Fim de jogo, você perdeu!")
    print(f"A palavra era: {palavra.title()}!")


if __name__ == "__main__":
    play()
