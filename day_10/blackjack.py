from random import randint

baralho = ['a', '2', '3', '4', '5', '6',
           '7', '8', '9', '10', 'j', 'q', 'k'] * 4


def play() -> None:
    """
    Starts a turn of blackjack
    """
    table = []
    player = []
    player_total = 0

    # Turn starts
    for _ in range(2):
        c1 = baralho.pop(randint(0, len(baralho)-1))
        table.append(c1)
        c2 = baralho.pop(randint(0, len(baralho)-1))
        player.append(c2)

    player_total = hand_value(player)

    # Main loop
    while True:
        if player_total == 21:
            win(player, table)
            break
        elif player_total > 21:
            print("BUST\n")
            loss(player, table)
            break
        else:
            print("Player: ", show_hand(player))
            print("Table: ", show_table_opening(table))

        print()
        choice = show_option()
        print()

        if choice == "hit":
            player = hit(player)

        elif choice == "stand":
            stand(player, table)
            break

        player_total = hand_value(player)
        print()


def hand_value(cards) -> int:
    """
    Returns the total value of a hand.
    """
    total = 0

    for card in cards:
        if total == 21:
            return total

        if card == 'a':
            # If total in hand is greater than 10, the value of an Ace will be 1
            total += 11 if total <= 10 else 1
        elif card in ['j', 'q', 'k']:
            total += 10
        else:
            total += int(card)

    return total


def show_option():
    """
    Show the options to hit or stand to the player
    """
    choice = input("[Hit] or [Stand]?\n-> ").lower()

    if choice == "hit" or choice == "stand":
        return choice
    else:
        print("Invalid option\n")
        return show_option()


def hit(hand):
    """
    Add a new card to the hand
    """
    hand.append(baralho.pop(randint(0, len(baralho)-1)))
    return hand


def stand(player, table):
    """
    The table starts drawing cards and verify they beat the player or not
    """
    p_total = hand_value(player)
    total = hand_value(table)

    while total < 17:
        table = hit(table)
        total = hand_value(table)
        if 'a' in table and total == 17:
            total -= 10

    if total > 21:
        win(player, table)

    elif total > p_total:
        loss(player, table)
    elif p_total > total:
        win(player, table)
    else:
        draw(player, table)


def show_table_opening(hand) -> str:
    """
    Display the hand of the table with the second card hidden
    """
    return f"{hand[0].title()} ? = {hand_value([hand[0]])}"


def show_hand(hand) -> str:
    """
    Display the complete hand
    """
    show = ''
    for c in hand:
        show += c.title() + " "
    return f"{show}= {hand_value(hand)}"


def win(player, table):
    """
    Shows victory message and finish the game
    """
    print("Player: ", show_hand(player))
    print("Table: ", show_hand(table))
    print()
    print("Congratulations, you win!")


def loss(player, table):
    """
    Shows defeat message and finish the game
    """
    print("Player: ", show_hand(player))
    print("Table: ", show_hand(table))
    print()
    print("Too bad, you lose!")


def draw(player, table):
    """
    Shows draw message and finish the game
    """
    print("Player: ", show_hand(player))
    print("Table: ", show_hand(table))
    print()
    print("It ended as a draw!")


if __name__ == '__main__':
    play()
