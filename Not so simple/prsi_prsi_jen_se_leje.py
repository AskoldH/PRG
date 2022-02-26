import random


class Deck():
    def __init__(self):
        # creating random mixed deck -> init deck
        card_values = ["ESO", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JUNÁK", "DÁMA", "KRÁL"]
        self.generated_deck = []

        not_used_card_values_hearts = card_values.copy()
        not_used_card_values_spades = card_values.copy()
        not_used_card_values_leaves = card_values.copy()
        not_used_card_values_diamonds = card_values.copy()

        while True:
            if not_used_card_values_hearts and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_hearts) - 1)
                self.generated_deck.append("♥" + not_used_card_values_hearts[random_int])
                del not_used_card_values_hearts[random_int]

            elif not_used_card_values_spades and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_spades) - 1)
                self.generated_deck.append("♠" + not_used_card_values_spades[random_int])
                del not_used_card_values_spades[random_int]

            elif not_used_card_values_diamonds and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_diamonds) - 1)
                self.generated_deck.append("♦" + not_used_card_values_diamonds[random_int])
                del not_used_card_values_diamonds[random_int]

            elif not_used_card_values_leaves and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_leaves) - 1)
                self.generated_deck.append("♣" + not_used_card_values_leaves[random_int])
                del not_used_card_values_leaves[random_int]

            elif not (len(not_used_card_values_spades) or len(not_used_card_values_diamonds) or len(
                    not_used_card_values_leaves) or len(not_used_card_values_hearts)):
                break

    def show_deck(self):
        print(self.generated_deck)

    def show_len(self):
        print(len(self.generated_deck))


class CardPile():
    def __init__(self, deck):
        # put one card on the top of pile -> init pile
        self.top_card = deck.pop(0)

    def put_card_on_top(self, deck, card, color=None):
        # check validity
        if self.top_card[0] == card[0] or self.top_card[1] == card[1] or color == card[0]:
            # put into deck
            deck.append(self.top_card)
            self.top_card = card
            # check for special cards
            if card[1] == '7':
                return 2
            elif card[0] == '♠' and card[1] == 'K':
                return 4
            elif card[1] == 'E':
                return "ace"
            elif card[1] == 'D':
                return "queen"
            return False

        # player casted off wrong card
        input(
            '\n' + f"No takhle to nepůjde!! {card} rozhodně nemůžeš dát na {self.top_card}! (Pro pokračování zmáčkni ENTER)")
        return card

    def show_top_card(self):
        print("\n" + f"Na vrcholu hromádky je karta {self.top_card}")


class HumanPlayer():
    def __init__(self):
        self.name = input(
            "Zdravím, vítej u snad všem známe hry prší, tentokrát ale v Pythonu!! Prosím zadej své jméno: ")
        self.card_deck = []

    # get card/cards from given deck
    def get_cards(self, deck, quantity=1):
        for i in range(0, quantity):
            self.card_deck.append(deck.pop(0))

    def show_cards(self):
        print("V ruce máš: ", end="")
        for card in self.card_deck:
            print(f"|{card}", end="")
        print("|")

    # from player deck pop card
    def put_card_into_pile(self, index):
        return self.card_deck.pop(index)

    def check_human_win(self):
        if not len(self.card_deck):
            print(f"\nMusím prohlásit, že {self.name} je velice dobrým hráčem prší, gratuluji vyhrál jsi!!")
            return True
        return False


class PCPlayer():
    def __init__(self):
        self.card_deck = []

    # get card/cards from given deck
    def get_cards(self, deck, quantity=1):
        for i in range(0, quantity):
            self.card_deck.append(deck.pop(0))

    def show_cards(self):
        for card in self.card_deck:
            print(f"|{card}", end="")
        print("|")

    # find most frequent color of card in pc deck
    def most_frequent(self):
        # is there simpler solution? I'm not happy with this one
        counter_hearts, counter_spades, counter_diamonts, counter_leaves = 0, 0, 0, 0
        for card in self.card_deck:
            if card[0] == '♥':
                counter_hearts += 1
            elif card[0] == '♦':
                counter_diamonts += 1
            elif card[0] == '♠':
                counter_spades += 1
            elif card[0] == '♣':
                counter_leaves += 1

        most_frequent = max([counter_diamonts, counter_leaves, counter_spades, counter_diamonts])

        if most_frequent == counter_hearts:
            return '♥'
        elif most_frequent == counter_diamonts:
            return '♦'
        elif most_frequent == counter_spades:
            return '♠'
        elif most_frequent == counter_leaves:
            return '♣'

    def check_pc_win(self):
        if not len(self.card_deck):
            return True
        return False

    def show_lose_for_player(self, player_deck):
        print(
            f"Obávám se, že jsi prohrál, počítač má prázdnou ruku ale ty v ní máš ještě {' '.join(str(x) for x in player_deck)}!!")


def main():
    while True:
        user_input = input("Pro novou hru zadej \"new\" a pro ukončení \"exit\": ")

        if user_input == "new":
            # init
            deck = Deck()
            human = HumanPlayer()
            pc = PCPlayer()
            pile = CardPile(deck.generated_deck)

            # get first 4 cards for player and pc
            human.get_cards(deck.generated_deck, 4)
            pc.get_cards(deck.generated_deck, 4)

            # basic setup
            player_move = True
            pc_move = True
            chosen_color = None

            while True:
                # win human
                if human.check_human_win():
                    break

                # win pc
                elif pc.check_pc_win():
                    pc.show_lose_for_player(human.card_deck)
                    break

                # human player move
                while player_move:
                    # reset pc_move after casting ace
                    pc_move = True

                    pile.show_top_card()
                    human.show_cards()
                    print(f"Počet karet tvého protivníka je {len(pc.card_deck)}!")
                    user_input = input(
                        "Zadejte pořadí karty, kterou chcete odhodit nebo \"vzít\" pro kartu z hromádky: ")

                    # user wanna get card from deck
                    if user_input == "vzít":
                        human.get_cards(deck.generated_deck, 1)
                        break

                    # check if input is number
                    try:
                        int(user_input)  # is there better solution?
                    except ValueError:
                        print("\n!!Zadejte správně pořadí karty nebo \"vzít\"(př. \"2\" pro kartu druhou z leva)!!")
                        continue

                    # check user input index validity
                    if int(user_input) - 1 > len(human.card_deck) or int(user_input) - 1 < 0:
                        print("!!Zadal jsi špatné pořadí mimo možnosti!!")
                        continue

                    # cast off card
                    returned_value = pile.put_card_on_top(deck.generated_deck,
                                                          human.put_card_into_pile(int(user_input) - 1),
                                                          chosen_color)

                    # reset chosen color after casting queen
                    chosen_color = None

                    # player put on top "attack" card
                    if returned_value == 2 or returned_value == 4:
                        pc.get_cards(deck.generated_deck, returned_value)
                        pc_move = False

                    # player casted off top ace
                    elif returned_value == "ace":
                        pc_move = False

                    # player casted queen
                    elif returned_value == "queen":
                        chosen_by_user = input(
                            "Po vyhození dámy si můžeš vybrat změnu barvy, vyber pomocí pořadí (♥-1, ♦-2, ♠-3, ♣-4):")
                        if chosen_by_user == '1':
                            chosen_color = '♥'
                        elif chosen_by_user == '2':
                            chosen_color = '♦'
                        elif chosen_by_user == '3':
                            chosen_color = '♠'
                        elif chosen_by_user == '4':
                            chosen_color = '♣'
                        else:
                            print("Po vyhození dámy jsi špatně vybral změnu barvy!")

                    # player casted off not valid card
                    elif returned_value:
                        human.card_deck.insert(int(user_input) - 1, returned_value)
                    continue

                # pc move
                while pc_move:
                    # reset player_move after casting ace
                    player_move = True

                    valid_card_found = False

                    # going through deck -> trying to find valid card
                    for card in pc.card_deck:
                        if card[0] == pile.top_card[0] or card[1] == pile.top_card[1]:
                            returned_value = pile.put_card_on_top(deck.generated_deck, card, chosen_color)
                            pc.card_deck.remove(card)

                            # reset chosen color
                            chosen_color = None

                            # pc put on top "attack" card
                            if returned_value == 2 or returned_value == 4:
                                human.get_cards(deck.generated_deck, returned_value)
                                player_move = False

                            # pc casted off top ace
                            elif returned_value == "ace":
                                player_move = False

                            elif returned_value == "queen":
                                chosen_color = pc.most_frequent()
                                print(f"Protivník změnil dámou barvu na \'{chosen_color}\!'")

                            valid_card_found = True
                            break

                    if not valid_card_found:
                        pc.get_cards(deck.generated_deck)  # valid card not found -> pc gets card
                    break
        elif user_input == "exit":
            print("Třeba příště, čau.")
            break

        else:
            print("Zadej to správně prosím!")


if __name__ == '__main__':
    main()
