import random
import guess_the_number_art
def guess_the_number(num, tries):
      while tries > 0:
            user_guess = int(input("Make a guess: "))
            if user_guess == num:
                  print(f"\nYou've guessed the number {num}. You Win!")
                  break
            elif user_guess < num:
                  tries -= 1
                  if tries > 0:
                        print("Too low.\nGuess again.")
                        print(f"\nYou have {tries} attempts remaining to guess the number.")
                  else:
                        print("Too low.")
                        print(f"\nYou have no more attempts. The number was {num}. You Lost!")
            else:
                  tries -= 1
                  if tries > 0:
                        print("Too high.\nGuess again.")
                        print(f"\nYou have {tries} attempts remaining to guess the number.")
                  else:
                        print("Too high.")
                        print(f"\nYou have no more attempts. The number was {num}. You Lost!")

print(guess_the_number_art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(1,100)
#print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
      attempts = 10
elif difficulty == "hard":
      attempts = 5

guess_the_number(number, attempts)