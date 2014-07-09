# Santase cards game
from random import shuffle
from os import system

"Coming back soon"

def all_cards():
    """
    The cards, return shuffle cards
    """
    titles = ["9", "10", "J", "Q", "K", "A"]
    colors = ["d", "c", "h", "s"]
    cards = []
    for title in titles:
        for color in colors:
            cards.append(title + color)
    shuffle(cards)
    return cards


def card_distribution(p1, p2):
    """
    Distributes cards to players
    """
    while len(p1["cards"]) < 6 or len(p2["cards"]) < 6:
        if len(p1["cards"]) < 6:
            p1["cards"].append(Cards.pop(-1))
        if len(p2["cards"]) < 6:
            p2["cards"].append(Cards.pop(-1))


def card_score(card):
    ''' Card type example "Kh", return score. if the card is trumb the cards is bigger then the others '''
    scores = {"9": 0, "10": 1, "J": 2, "Q": 3, "K": 4, "A": 5}
    score = scores[card[:-1]]
    if card[-1] == trumb[-1][-1]:
        return score + 10
    else:
        return score
    
    
def card_given(player, card):
    while True:
        try:
            player["cards"].remove(card)
            player["given"] = card
            return True
        except ValueError:
            gui()
            print "You don't have the card %s\n Please check and try again!" % card
            return False


def card_withdraw(player):
    player.append(Cards.pop(-1))


def input(msg):
    return raw_input(msg + ">>>> ::: ")


def menu(game = 0):
    system('clear')
    if game:
        print "\t\t\tWelcome to the Santase Card Game\n\n\n"
        print """\t%s
            \nCards: %s\nHands: %s\nScore: %s\t Card given: %s
            \n\n\t%s
            \nCards: %s\nHands: %s\nScore: %s\tCard given: %s""" % (player1["name"], ' '.join(player1["cards"]), ' '.join(player1["hands"]), player1["score"], player1["given"], player2["name"], ' '.join(player2["cards"]), ' '.join(player2["hands"]), player2["score"], player2["given"])
        print "\nTRUMB: %s\nCards left: %s\t%s" % ("".join(trumb), len(Cards), "#" * (len(Cards)))
    print """\n\nMENU\n\n(New) - Will start new game\n\n(S)tart - will start the game(Exit)"""


def turn_change(player):
    player["turn"] = 1


def hand_append(player, card1, card2):
    player["hands"].append(card1)
    player["hands"].append(card2)


def check(player1_score, player2_score):

    if card_score(player1_score) > card_score(player2_score):
        turn_change(player1)
        hand_append(player1, player1_score, player2_score)
        card_distribution(player1, player2)
        gui()
        print "%s win the hand" % player1["name"]
    if card_score(player1_score) < card_score(player2_score):
        turn_change(player2)
        hand_append(player2, player2_score, player1_score)
        card_distribution(player2, player1)
        gui()
        print "%s win the hand" % player2["name"]


def whose_turn(): #TODO: help
    while len(player1["cards"]) > 0 or len(player2["cards"]) > 0:
        
        Cards.insert(0, Cards.pop(-1)) # To implement with if statement
        if player1["turn"] == 1:
            player1_score = player_turn(player1)
            player2_score = player_turn(player2)
            check(player1_score, player2_score)
        if player2["turn"] == 1:
            player2_score = player_turn(player2)
            player1_score = player_turn(player1)
            check(player1_score, player2_score)


def game(player):
    while True:  # TODO: help 2 :)
        if card_given(player, input(player["name"] + "'s turn")):
            print "\n\nCard given by %s: %s\n\n" %(player["name"], player["given"])
            gui()
            return player["given"]


def main():
    Cards = []
    player1 = {"name": "", 'cards': [], 'turn': 1, 'given': 0, 'score': 0, 'hands':
    [], "totalscore": 0}
    player2 = {"name": "", 'cards': [], 'turn': 0, 'given': 0, 'score': 0, 'hands':
        [], "totalscore": 0}
    color = ""
    while True:
        menu()
        
        if choice == "s" or choice == "S":
            if not player1["name"] or not player2["name"]:
                player1["name"] = raw_input("Please type player 1 name: ")
                player2["name"] = raw_input("Please type player 2 name: ")
            Cards = all_cards()
            trumb = Cards[0]
            gui()
            game()
        elif player1["name"] or player2["name"]:
            print "(C)ontinue the game!"
        elif choice == "c" or choice == "C":
            print "ok"
        elif choice == "exit" or choice == "EXIT":
            exit()
        choice = input("")

if __name__ == "__main__":
    main()


