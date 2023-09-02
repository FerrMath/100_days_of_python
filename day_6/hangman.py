from random import choice
from hangman_art import stages, logo
from palavras import palavras_aleatorias as p


def play():
    # Quantidade de vidas restantes
    vidas = len(stages)

    # Escolhendo a palavra secreta
    palavra_secreta = choice(p)

    # Letras escolhidas pelo usuario
    letras = set()

    print(logo,"\n")

    # Loop principal do jogo
    while True:
        letra = input("Digite uma letra: ").lower()
        letras.add(letra)
        
        if letra not in palavra_secreta:
            vidas = reduzir_vida(vidas)
            mostrar_erro(vidas, letra)
            if vidas == 0:
                fim_de_jogo_derrota(palavra_secreta)
                return
            exibir_tentativa(letras, palavra_secreta)
        else:
            if acertou_palavra(palavra_secreta, letras):
                fim_de_jogo_vitoria(palavra_secreta)
                return
            exibir_tentativa(letras, palavra_secreta)


def exibir_tentativa(tentativas:set[str], palavra):
    print()
    entradas = ["_" if letra not in tentativas else letra for letra in palavra]
    print("".join(entradas))


def reduzir_vida(vidas):
    return vidas - 1


def mostrar_erro(vidas: int, letra: str):
    print(stages[vidas])
    print(f"A letra \"{letra}\" não está na palavra")
    print()


def acertou_palavra(palavra, letras):
    tentativa = ["_" if letra not in letras else letra for letra in palavra]
    return "".join(tentativa) == palavra


def fim_de_jogo_vitoria(palavra:str):
    print()
    print("Fim de jogo, você ganhou!")
    print(f"A palavra era: {palavra.title()}!")


def fim_de_jogo_derrota(palavra: str):
    print()
    print("Fim de jogo, você perdeu!")
    print(f"A palavra era: {palavra.title()}!")


if __name__ == "__main__":
    play()
