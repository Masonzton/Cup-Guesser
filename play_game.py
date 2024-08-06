import random
import itertools
from typing import List

NUMBER_OF_DIGITS = 4
ALL_POSSIBLE_CODES = list(itertools.permutations(range(1, NUMBER_OF_DIGITS + 1)))


def get_random_code(N):
    numbers = list(range(1, N + 1))
    random.shuffle(numbers)
    return numbers


def get_number_correct(array, guess):
    correct = 0
    for index in range(len(array)):
        if int(array[index]) == int(guess[index]):
            correct += 1

    return correct


def guess_to_array(guess) -> List[int]:
    return [int(i) for i in guess]


def print_guess_distribution(remaining_codes: List[List[int]]) -> List[List[int]]:
    """For each guess, there will be a certain distribution of 0,1,2, or 4 correct
    cups. A guess is good when it has a good spread on this distribution. This is because
    you want there to be the least number of remaining possible guesses. So the ideal guess
    is the one with the smallest maximum"""
    print(
        "Distribution of correct cups: number of guesses that achieve this distribution"
    )
    distributions = {}
    for guess in ALL_POSSIBLE_CODES:
        # number of codes in each category of number correct
        distribution = [0, 0, 0, 0, 0]
        # see how many would be eliminate at this step given the remaining codes
        for code in remaining_codes:
            number_correct = get_number_correct(code, guess)
            distribution[number_correct] += 1
        distribution = tuple(distribution)
        if distribution in distributions:
            distributions[distribution].append(guess)
        else:
            distributions[distribution] = [guess]
    smallest_maximum = None
    best_distribution = None
    for distribution, codes in distributions.items():
        maximum = max(distribution)
        if smallest_maximum is None or maximum < smallest_maximum:
            smallest_maximum = maximum
            best_guess = codes[0]
            best_distribution = distribution
        elif maximum == smallest_maximum:
            # it is better to have a guess in the all correct category
            if distribution[-1] >= best_distribution[-1]:
                smallest_maximum = maximum
                best_guess = codes[0]
                best_distribution = distribution

        print(f"{distribution}: {len(codes)} example: {codes[0]}")

    print(f"greedy guess: {best_guess}")


def is_guess_valid(guess: str) -> bool:
    is_valid = True
    is_valid &= len(guess) == NUMBER_OF_DIGITS
    for number in guess:
        is_valid &= number.isnumeric()
        if number.isnumeric():
            is_valid &= int(number) <= NUMBER_OF_DIGITS
            is_valid &= int(number) > 0

    return is_valid


def play_game(debug=False):
    if debug:
        remaining_codes = list(itertools.permutations(range(1, NUMBER_OF_DIGITS + 1)))
    actual_numbers = get_random_code(NUMBER_OF_DIGITS)

    # print(f"Secret Numbers are: {actual_numbers}")

    while 1:
        if debug:
            print_guess_distribution(remaining_codes)

        # ask for input
        example_string = "".join([str(x) for x in range(1, NUMBER_OF_DIGITS + 1)])
        guess = input(
            f"\n\nInput Guess, numbers 1 to {NUMBER_OF_DIGITS}. i.e. {example_string}:  "
        )
        if guess == "q":
            break

        if not is_guess_valid(guess):
            print("invalid guess string. Valid example is 1234")
            continue
        number_correct = get_number_correct(actual_numbers, guess)

        # take away possible codes
        if number_correct == len(actual_numbers):
            print("You win!!")
            break
        print(f"{number_correct} Are correct")

        if debug:
            remaining_codes = [
                code
                for code in remaining_codes
                if get_number_correct(guess, code) == number_correct
            ]
            print(f"Total Remaining Codes: {len(remaining_codes)}")
            print("Reaming codes are:")
            for code in remaining_codes:
                print(code)

    print(f"Actual Array was: {actual_numbers}")


if __name__ == "__main__":
    play_game(False)
