#! python3
from random import randint


def number_guess(secret_number):
    """
    Run a guessing game; asks user for input and displays either "too low" or "too high".
    :param secret_number: 
    :return: None
    """
    while True:
        try: 
            guess = int(input("Zgadnij liczbę:"))
        except ValueError:
            print("To nie jest liczba.")
            continue

        if int(guess) < secret_number:
            print("Za mało!")
        elif int(guess) > secret_number:
            print("Za dużo!")
        elif int(guess) == secret_number:
            print("Zgadłeś!")
            break
    return


if __name__ == "__main__":
    number_guess(randint(0, 500))
