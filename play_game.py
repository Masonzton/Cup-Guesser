import random
import itertools
from typing import List, Tuple

ALL_POSSIBLE_CODES = list(itertools.permutations(range(1, 4+1)))

def random_permutation(N):
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
    for distribution, codes in distributions.items():
        print(f"{distribution}: {len(codes)} {codes}")

history : List[Tuple[List[int], int]] = []

remaining_codes = list(itertools.permutations(range(1, 4+1)))

actual_numbers = random_permutation(4)
print(f"Secret Numbers are: {actual_numbers}")
while 1:
    print_guess_distribution(remaining_codes)

    #TODO: validate input
    # ask for input
    guess = input("\n\nInput Guess, numbers 1 to 4:  ")
    if guess == "q":
        break

    number_correct = get_number_correct(actual_numbers, guess)

    history.append((guess_to_array(guess), number_correct))

    # take away possible codes
    remaining_codes = [code for code in remaining_codes if get_number_correct(guess, code) == number_correct]
    if number_correct == len(actual_numbers):
        print("You win!!")
        break
    print(f"{number_correct} Are correct")
    print(f"Total Remaining Codes: {len(remaining_codes)}")
    print(f"Reaming codes are:")
    for code in remaining_codes:
        print(code)

print(f"Actual Array was: {actual_numbers}")
