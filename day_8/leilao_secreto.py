import os

def leilao():
    lances = dict()

    print("Welcome to the secret auction program!")

    while True:
        apostador = input("What is your name?: ")
        lance = float(input("What's your bid?: $"))
        lances[apostador] = lance
        continuar = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        while continuar != "yes" and continuar != "no":
            print("Invalid value!")
            continuar = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if continuar == 'yes':
            limpar_tela()
            continue
        elif continuar == 'no':
            break
    check_winner(lances)


def check_winner(lances):
    maior_valor = 0
    apostador = ""

    for key, valor in lances.items():
        if valor > maior_valor:
            maior_valor = valor
            apostador = key
    limpar_tela()
    print(f"The winner is {apostador}, with the bid of ${maior_valor:.2f}")
    return


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    leilao()