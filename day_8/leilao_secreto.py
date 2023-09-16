import os
from art import logo

def auction():
    lances = dict()

    print("Welcome to the secret auction program!")

    while True:
        apostador = input("What is your name?: ")
        lance = float(input("What's your bid?: $"))
        lances[apostador] = lance
        continue_str = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        
        while continue_str != "yes" and continue_str != "no":
            print("Invalid value!")
            continue_str = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        
        if continue_str == 'yes':
            clear_screen()
            continue
        elif continue_str == 'no':
            break
    
    check_winner(lances)


def check_winner(lances):
    highest_bid = 0
    bidder = ""

    for key, valor in lances.items():
        if valor > highest_bid:
            highest_bid = valor
            bidder = key
    
    clear_screen()
    print(f"The winner is {bidder}, with the bid of ${highest_bid:.2f}")
    return


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    print(logo + "\n")
    auction()