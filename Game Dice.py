#! python3
from random import randint
import re


def dice_input(requested_dice):
    """
    This function takes 'dice code' as user input (e.g. 2d6+3) and verifies its correctness using regular expressions.
    Non-allowed dice are filtered out. Then the correct result is split into key variables which are fed to dice-rolling
    function.
    :param requested_dice: string, dice code
    :return: direct call to function roll with three arguments: no. of dice, type of dice, modifier
    """
    allowed_dice = (3, 4, 6, 8, 10, 12, 20, 100)

    dice_regex = re.compile(r"""
        ^(
            (\d*)?      # optional no. of dice
            (d)         # required letter d
            (\d+)       # required dice type
            (           # optional modifier group
                (\+|\-)     # modifier type
                (\d*)       # modifier size
            )?
        )$
        """, re.VERBOSE | re.IGNORECASE)
    result = dice_regex.search(requested_dice)

    if result is not None:

        if int(result[4]) not in allowed_dice:
            return f"No such die! Only {allowed_dice} are allowed."

        dice_count = 1
        if result[2] != "":
            dice_count = int(result[2])
        else:
            dice_count = 1

        dice_type = int(result[4])

        modifier = 0
        if result[5] is not None:
            if result[6] == "+":
                modifier = int(result[7])
            elif result[6] == "-":
                modifier = -1 * int(result[7])

        return roll(dice_count, dice_type, modifier)
    else:
        return "No such die!"


def roll(dice_count, dice_type=6, modifier=0):
    """
    Simulates dice rolling, including: no. of dice, dice type, adds value modifies to total result.
    Under allowed_dice defines permitted dice types. Dice 20 not permitted!!!
    :param dice_count: Integer, number of dice
    :param dice_type: Integer, type of dice (no. of sides)
    :param modifier: Integer, result modifier added to total
    :return: Integer, total result
    """

    dice_result = 0

    for d in range(dice_count):
        dice_result += randint(1, dice_type)
    dice_result += modifier
    return dice_result


if __name__ == "__main__":
    print("Test dla 2d6+1", dice_input("2d6+1"))
    print("Test dla 2d10+20:", dice_input("2D10+20"))
    print("Test dla 2d10:", dice_input("2D10"))
    print("Test dla 3d6-3:", dice_input("3D6-3"))
    print("Test dla 1d11:", dice_input("1d11"))
    print("Test dla jednej 6:", dice_input("d6"))
    print("Test dla string:", dice_input("test"))
