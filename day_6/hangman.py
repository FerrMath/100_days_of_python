from random import choice

palavras_aleatorias = [
    "python", "computador", "praia", "montanha",
    "música", "livro", "esportes", "arte", "ciência",
    "viagem", "família", "amigos", "comida",
    "tecnologia", "natureza", "filme",
    "história", "aventura", "sonho"
]

# Escolhendo a palavra secreta
palavra_secreta = choice(palavras_aleatorias)

# Letras escolhidas pelo usuario
letras: set[str] = set()

# Gerando área de input do usuario
entradas = ["_" if letra not in letras else letra for letra in palavra_secreta]
print(letras, entradas)

def exibirTentativa(tentativas:set[str]):
    entradas = ["_" if letra not in tentativas else letra for letra in palavra_secreta]
    print("".join(entradas))

# Loop principal do jogo
# TODO criar logica para acompanhar quantidade de vidas disponivel para o jogador
while True:
    letra = input("Digite uma letra: ")
    letras.add(letra)
    exibirTentativa(letras)


