from game_data import data
from art import vs, logo
import random

def wrong_input():
    print("\nWrong input. Please type 'A' or 'B'.")

def print_data(random):
    if random == random_A:
        a_or_b = "A"
        print(f"Compare {a_or_b}: {random['name']}, a {random['description']}, from {random['country']}")
    else:
        # random == random_B
        a_or_b = "B"
        print(f"Against {a_or_b}: {random['name']}, a {random['description']}, from {random['country']}")

def print_logo(versus):
    print(versus)

def winner_is(rand_A, rand_B):
    if rand_A["follower_count"] > rand_B["follower_count"]:
        winner = "A"
    else:
        winner = "B"
    return winner

def generate_random_B():
    random_key = random.sample(data, 1)
    return random_key[0]

def game_over():
    isTrue = False
    print(f"\nSorry, that's wrong. Your final score is: {score}.")
    return isTrue

# Random A, Random B
score = 0
random_keys = random.sample(data, 2)
random_A = random_keys[0]
random_B = random_keys[1]
winner = winner_is(random_A, random_B)
isTrue = True

print_logo(logo)

while(isTrue):
    print_data(random_A)
    print_logo(vs)
    print_data(random_B)
    guess = input(f"Who has more followers? Type 'A' or 'B': ").capitalize()
    if guess == "A" or guess == "B":
        if guess == winner:
            score += 1
            print("\n" * 10)
            print_logo(logo)
            print(f"\nYou're right! Current score: {score}.")
            if winner == "A":
                random_B = generate_random_B()
                while random_B == random_A:
                    random_B = generate_random_B()
                winner = winner_is(random_A, random_B)
            else:
                random_A = random_B
                random_B = generate_random_B()
                winner = winner_is(random_A, random_B)
        else:
            isTrue = game_over()
    else:
        wrong_input()
