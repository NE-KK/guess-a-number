import random

searched_number = random.randint(1, 100)
is_won = False

print(searched_number)


while not is_won:
    guessed_number = int(input("Guess a number between 1 and 100: "))

    if guessed_number > searched_number:
        print(f"{guessed_number} is to high!")
    elif guessed_number < searched_number:
        print(f"{guessed_number} is to low!")
    else:
        print(f"Congratulations. {guessed_number} is correct.")
        is_won = True

print("END")
