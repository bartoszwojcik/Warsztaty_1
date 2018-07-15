#! python3
class RangeError(Exception):
    pass


def auto_guess():
    """
    This function tries to guess a number from range 1-1000 by splitting the range into two equal parts. Guessing is
    done by utilizing hints provided by the user.
    :return: String "Wygrałem", only if won.
    """
    min = 0
    max = 1000
    guess = 0
    for i in range(0, 10):
        guess = int((max - min) / 2) + min
        print("Zgaduję:", guess)
        while True:
            response = input()
            if response.lower() == "zgadłeś":
                print("Wygrałem!")
                return
            elif response.lower() != "za mało" and response.lower() != "za dużo" and response.lower() != "zgadłeś":
                print("Nie znam tej odpowiedzi.")
            elif response.lower() == "za dużo":
                max = guess
                break
            elif response.lower() == "za mało":
                min = guess
                if i == 9:
                    print("Nie oszukuj!")
                    continue
                break
    print("")


if __name__ == "__main__":
    while True:
        try:
            secret = int(input("Pomyśl liczbę od 0 do 1000, a ja zgadnę w max. 10 próbach."))
            if secret < 1 or secret > 1000:
                raise RangeError
            else:
                break
        except ValueError:
            print("Tylko integer.")
        except RangeError:
            print("Tylko w zakresie 1 do 1000")

    auto_guess()
