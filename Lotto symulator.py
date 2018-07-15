#! python3
from random import shuffle


class RangeException(Exception):
    pass


class DoubleException(Exception):
    pass


def lotto_input():
    """
    Function for taking 6 values from user. Checks if proper ints, value in range and whether values are not repeated.
    Warning: Requires custom classes: RangeException and Double Exception
    :return: sorted list of selected numbers
    """
    numbers_words = ("pierwszą", "drugą", "trzecią", "czwartą", "piątą", "szóstą")
    number_input = []
    while len(number_input) < 6:
        print("Podaj", numbers_words[len(number_input)], "liczbę:")
        while True:
            try:
                value = int(input())
                if value < 1 or value > 49:
                    raise RangeException
                if value in number_input:
                    raise DoubleException
                number_input.append(value)
                break
            except ValueError:
                print("Wartość nie jest liczbą. Tylko liczby naturalne.")
            except RangeException:
                print("Liczba nie jest w zakresie 1-49.")
            except DoubleException:
                print("Ta liczba została już wybrana.")
    number_input.sort()
    print("Wybrane liczby:", number_input)
    return number_input


def lotto_random():
    """
    Generates random Lotto results: 6 numbers.
    :return: sorted list of results
    """
    possible_numbers = tuple([i for i in range(1, 50)])     #Tuple to prevent modification
    randomization = list(possible_numbers)
    shuffle(randomization)
    randomization = randomization[:6]
    randomization.sort()
    print("Wyniki dzisiejszego losowania to:", randomization)
    return randomization


def lotto_result_check(num_input, num_random):
    """
    Verify if user's numbers match Lotto results. Three matches are needed
    :param num_input: List of user-selected numbers
    :param num_random: List of Lotto results
    :return: None
    """
    match_counter = 0
    result_dict = ["trójkę", "czwórkę", "piątkę", "szóstkę"]
    for i in range(len(num_input)):
        if num_input[i] in num_random:
            match_counter += 1
    if match_counter < 3:
        print("Niestety, nie trafiłeś/aś nawet trójki. :(")
    else:
        print("Gratulacje! Trafiłeś/aś", result_dict[match_counter - 3])
    return


if __name__ == "__main__":
    lotto_result_check(lotto_input(), lotto_random())
