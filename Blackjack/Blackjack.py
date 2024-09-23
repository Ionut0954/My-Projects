import random

class Colours():
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"

def remove_cards_from_deck(drawn_cards):
    """Removes drawn cards from the deck"""
    for card_to_be_removed in drawn_cards:
        deck.remove(card_to_be_removed)

def calculate_score(drawn_cards):
    """Calculate the score of user's/computer's drawn cards"""
    total_score = 0
    for card in drawn_cards:
        if type(card) is not int:
            if card == "J" or card == "Q" or card == "K":
                card = 10
                total_score += card
            elif card == "A":
                if total_score + 11 <= 21:
                    card = 11
                    total_score += card
                else:
                    card = 1
                    total_score += card
        else:
            total_score += card
    return total_score

def draw_card():
    """Returns a random card from the deck and removes it from the deck"""
    drawn_card = random.choices(deck)
    remove_cards_from_deck(drawn_card)
    return drawn_card

# Start
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
user_score = 0
computer_score = 0
user_has_blackjack = False
computer_has_blackjack = False
# User's first 2 cards
user_cards = random.choices(deck, k=2)
remove_cards_from_deck(user_cards)
user_score = calculate_score(user_cards)
if user_score == 21:
    user_has_blackjack == True

print(f"Your cards: {user_cards}, current score: {user_score}")

# Computer's first 2 cards
computer_cards = random.choices(deck, k=2)
remove_cards_from_deck(computer_cards)
print(f"Computer's first card: {computer_cards[0]}")
computer_score = calculate_score(computer_cards)
if computer_score == 21:
    computer_has_blackjack = True

# Check if user and/or computer have Blackjack
if user_has_blackjack and computer_has_blackjack:
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(f"\n{Colours.BLUE}You both have Blackjack! It's a Draw!")
elif user_has_blackjack:
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(f"\n{Colours.GREEN}Blackjack! You Win!")
elif computer_has_blackjack:
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(f"\n{Colours.RED}Computer has Blackjack! You lose!")

# User's turn to draw cards
else:
    while user_score < 21:
        another_card = input("Type 'y' to get another card or type anything else to pass: ").lower()
        if another_card == "y":
            drawn_card = draw_card()
            for card in drawn_card:
                user_cards.append(card)
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
        else:
            break
    # Game ends if user's score is >= 21
    print(f"\nYour final hand: {user_cards}, final score: {user_score}\n")
    if user_score > 21:
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(f"\n{Colours.RED}You Lose!")
    elif user_score == 21:
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(f"\n{Colours.GREEN}You Won!")

    # Computer's turn to draw cards
    else:
        while computer_score < 17:
            computer_drawn_card = draw_card()
            for card in computer_drawn_card:
                computer_cards.append(card)
            computer_score = calculate_score(computer_cards)

        if computer_score < 22:
            if computer_score == 21:
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(f"\n{Colours.RED}Computer Won!")
            elif computer_score > user_score:
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(f"\n{Colours.RED}Computer Won!")
            elif computer_score == user_score:
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(f"\n{Colours.BLUE}It's a Draw!")
            else:
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(f"\n{Colours.GREEN}You Won!")
        else:
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(f"\n{Colours.GREEN}You Won!")
