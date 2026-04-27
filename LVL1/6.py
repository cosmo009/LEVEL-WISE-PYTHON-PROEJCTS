import random

power = True

while power:
    answer = random.randint(1, 100)

    print("\n\n---NUMBER GUESSING GAME---")
    print("RULES:")
    print("1. Guess a number between 1 - 100.")
    print("2. EASY - 10 , MEDIUM - 5 , HARD - 3 , IMPOSSIBLE - 1")

    # Difficulty selection
    while True:
        try:
            difficulty = input("\nChoose a difficulty (E/M/D/I): ").upper()
        except ValueError:
            print("Invalid input. Enter a valid difficulty.")
            continue
        finally:
            if difficulty == "E":
                guesses = 10
                break
            elif difficulty == "M":
                guesses = 5
                break
            elif difficulty == "D":
                guesses = 3
                break
            elif difficulty == "I":
                guesses = 1
                break
            else:
                print("Invalid choice. Try again.")

    remaining_guesses = guesses

    while remaining_guesses > 0:
        try:
            user_guess = int(input("\nGuess a number between 1 - 100: "))
            remaining_guesses -= 1

            if user_guess<0 or user_guess>100:
                print("Well that was fucking stupid, to make a guess out of the RANGE 1 - 100.")
            elif 0 < user_guess < answer:
                print(f"Too low! Guesses left: {remaining_guesses}")
            elif answer < user_guess < 100:
                print(f"Too high! Guesses left: {remaining_guesses}")
            elif user_guess == answer:
                print(f"Correct! The number was {answer}")
                break

        except ValueError:
            print("Invalid input. Enter a number.")

    else:
        print(f"Game Over! The number was {answer}.\nGuesses Left = {remaining_guesses}.")

    # Play again
    while True:
        ask_end = input("\nPLAY AGAIN? (Y/N): ").upper()
        if ask_end == "Y":
            break
        elif ask_end == "N":
            power = False
            break
        else:
            print("Invalid choice.")