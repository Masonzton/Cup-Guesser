"""Test the greedy strategy"""
from typing import List, Dict, Tuple
import itertools

NUMBER_OF_DIGITS = 4
ALL_POSSIBLE_CODES = list(itertools.permutations(range(1, NUMBER_OF_DIGITS+1)))

def get_number_correct(code, guess):
    correct = 0
    for index in range(len(code)):
        if code[index] == guess[index]:
            correct += 1
    
    return correct


def get_distributions(remaining_codes: List[List[int]]) -> Dict[Tuple[int], List[List[int]]]:
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

    return distributions

def get_greedy_guess(distributions: Dict[Tuple, List[List[int]]]) -> List[int]:
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
    
    return best_guess

def get_filter_codes(remaining_codes, guess, number_correct):
    filtered_codes = []
    for code in remaining_codes:
        if get_number_correct(code, guess) == number_correct:
            filtered_codes.append(code)
    return filtered_codes

def main():
    # simulate greedy guessing for every possible actual code
    worst_case_guesses = None
    total_codes = len(ALL_POSSIBLE_CODES)
    for actual_code in ALL_POSSIBLE_CODES:
        number_of_guesses = 0
        remaining_codes = ALL_POSSIBLE_CODES
        while number_of_guesses < total_codes:
            distribution = get_distributions(remaining_codes)
            guess = get_greedy_guess(distribution)

            # for distribution, codes in distribution.items():
            #     print(f"{distribution}: {len(codes)} example: {codes[0]}")

            number_correct = get_number_correct(actual_code, guess)
            number_of_guesses+=1

            # print(f"guess: {guess}, number correct: {number_correct}")

            if number_correct == NUMBER_OF_DIGITS:
                break
            
            remaining_codes = get_filter_codes(remaining_codes, guess, number_correct)
        
        print(f"code: {actual_code}, number_of_guesses: {number_of_guesses}")
        
        if worst_case_guesses is None or number_of_guesses > worst_case_guesses:
            worst_case_guesses = number_of_guesses
    
    print(f"worst case is {worst_case_guesses} guesses with greedy strategy")


if __name__ == "__main__":
    main()