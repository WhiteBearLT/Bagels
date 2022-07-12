import random

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_num() -> str:
    """return str of unique nums. Whose len is NUM_DIGITS"""
    nums = list(range(10))
    random.shuffle(nums)

    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(nums[i])
    return secret_num


def get_clues(guess, secret_num) -> str or list:
    """return str with hints for player"""
    if guess == secret_num:
        return 'You guess it!'

    clues = []
    for i in range(len(guess)):
        if guess == secret_num[i]:
            clues.append('So hot!')
        elif guess[i] in secret_num:
            clues.append('So warm!')
    if len(clues) == 0:
        return 'So cold!'

    clues.sort()
    return ' '.join(clues)


def is_only_digits(num) -> bool:
    """return True if num - str consists of numbers, else return False"""
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


def start():
    print(f'I guess a {NUM_DIGITS} digit number that you must guess!'
          f'\nI give you some hints...'
          f'\nWhen I say:   that\'means:'
          f'\nCold!         No one number guessed.'
          f'\nWarm!         One number guessed, but its position is not guessed.'
          f'\nHot!          One number and its position are guessed.')

    while True:
        secret_num = get_secret_num()
        print(f'So, I guessed a number. You have {MAX_GUESS} attempts to guess it.')

        guess_taken = 1
        while guess_taken <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not is_only_digits(guess):
                print(f'Attempt {guess_taken}')
                guess = input('Input 3-digit number: ')

            print(get_clues(guess, secret_num))
            guess_taken += 1

            if guess == secret_num:
                break
            if guess_taken > MAX_GUESS:
                print(f'There are no more attempts. I guess the number is {secret_num}')

        if not input('Do you want play again? (yes or no) ').lower().startswith('y'):
            break


if __name__ == '__main__':
    start()
