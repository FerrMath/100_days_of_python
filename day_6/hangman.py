from random import choice
from hangman_art import stages, logo
from palavras import palavras_aleatorias as p
import string as s


def play():
    vidas = len(stages)
    palavra_secreta = choice(p)
    letras = set()

    # Exibindo a logo do jogo
    print(logo,"\n")

    # Loop principal do jogo
    while True:
        letra = input("Digite uma letra: ").lower()

        # Verifica se letra digitada é valida e não é repetida
        while len(letra) > 1 or letra not in s.ascii_lowercase or letra == "" or letra in letras:
            if letra in letras:
                print(f"Você já digitou a letra \"{letra}\", tente outra vez com uma letra diferente!\n")
            else:
                print("Tentativa invalida, tente outra vez!\n")
            letra = input("Digite uma letra: ").lower()

        letras.add(letra)

        # Verifica se letra está na palavra digitada
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
