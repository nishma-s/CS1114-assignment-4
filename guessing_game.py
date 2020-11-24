# Author: Nishma Shakya
# Assignment #4 - Guessing Game
# Date due: 2020-11-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT CODE BELOW (changing MAX_MISSES is ok) ########
import random
import sys

MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1


def display_game_state(chars, misses):
    """
    Displays the current state of the game: the list of characters to display
    and the list of misses.
    """

    print()
    print('=' * BORDER_LENGTH)
    print()

    print("Word:\t{}\n".format(space_chars(chars)))
    print("Misses:\t{}\n".format("".join(misses)))


####### DO NOT EDIT CODE ABOVE (changing MAX_MISSES is ok) ########

def blank_chars(word):
    """Returns a list of underscore characters with the same length as word.

    :param word: target word as a string
    :return: a list of underscore characters ('_')

    >>> blank_chars("happiness")
    ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    """
    word_length = len(word)
    blank_lst = []
    if word == "":
        return blank_lst
    else:
        for letter in range(word_length):
            blank_lst.append("_")
        return blank_lst


def space_chars(chars):
    """Returns a string with the characters in chars list separated by spaces.

    :param chars: a list of characters
    :return: a string containing characters in chars with intervening spaces

    >>> space_chars(['h', '_', 'p', 'p', '_', 'n', '_', '_', '_'])
    'h _ p p _ n _ _ _'
    """
    new_lst = []
    string_chars = ""
    for letter in chars:
        if len(chars) == 0:
            new_lst.append(" ")
        elif len(chars) == 1:
            new_lst.append(letter)
        else:
            new_lst.append(letter)
            new_lst.append(" ")
    if len(new_lst) > 1:
        new_lst.pop()
        # this removes the extra space at the end
    for char in new_lst:
        string_chars += char
        # this is a method of turning the list into a string
    return string_chars


def get_guess():
    """Prompts the user for a guess to check for the game's current word. When the user
    enters input other than a single character, the function prompts the user again
    for a guess. Only when the user enters a single character will the prompt for
    a guess stop being displayed. The function returns the single-character guess
    entered by the user.

    :return guess: a single character guessed by user
    """
    user_guess = input("Guess:\t")
    while len(user_guess) > 1 or user_guess.isalpha() == False:
        user_guess = input("Guess:\t")
    return user_guess.lower()


def check_guess(word, guess):
    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.


    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions
    """
    word_lst = list(word)
    count_guess = []
    for i in range(len(word_lst)):
        if word_lst[i] == guess:
            count_guess.append(i)
    return count_guess


def update_chars(chars, guess, positions):
    """Updates the list of characters, chars, so that the characters
    at the index values in the positions list are updated to the
    character guess.


    :param chars: a list of characters
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    for idx in positions:
        chars[idx] = guess


def add_to_misses(misses, guess):
    """Adds the character guess to the misses list.

    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :return: None
    """
    misses.append(guess)


def update_state(chars, misses, guess, positions):
    """Updates the state of the game based on user's guess. Calls the function update_chars() when
    the positions list is not empty to reveal the indices where the character guess is present. Calls the
    function add_to_misses() when the positions list is empty to add guess to the misses list.

    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    if len(positions) > 0:
        update_chars(chars, guess, positions)
    else:
        add_to_misses(misses, guess)


def is_round_complete(chars, misses):
    """Indicates whether or not a round has ended. This function returns True
    when the user has successfully guessed the target word or exceeds the
    number of allowed misses. Otherwise, the function returns False,
    indicating that the round is not complete. A message revealing the
    user's success or failure guessing the target word is output by this
    function when the round is complete.


    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :return status: True when round is finished, False otherwise
    """
    if len(misses) > MAX_MISSES and "_" in chars:
        # print()
        print("\nSORRY! NO GUESSES LEFT.")
        return True
    elif "_" not in chars and len(misses) <= MAX_MISSES:
        # print()
        print("\nYOU GOT IT!")
        return True
    elif len(misses) > MAX_MISSES:
        # print()
        print("\nSORRY! NO GUESSES LEFT.")
        return True
    elif "_" not in chars:
        # print()
        print("\nSORRY! NO GUESSES LEFT.")
        return True
    else:
        return False


def read_words(filepath):
    """Opens a file of word located at filepath, reads the file of words line by line,
    and adds each word from the file to a list. The list is returned by the
    function

    :param filepath: path to input file of words (one per line)
    :return word_list: list of strings contained in input file
    """
    word_file = open(filepath, "r")
    words_lst = []
    for line in word_file:
        words_lst.append(line.strip('\n'))
    return words_lst


def get_word(words):
    """Selects a single word randomly from words list and returns it.

    :param words: list of strings
    :return word: string from words list
    """
    rand_idx = random.randrange(0, len(words) - 1)
    return words[rand_idx]


def is_game_complete():
    """Prompts the user with "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.

    :return response: boolean representing game completion status
    """
    play_again = input("Play again (Y/N)? ")
    while play_again != "Y" or play_again != "y" or play_again != "N" or play_again != "n":
        if play_again == "Y" or play_again == "y":
            return False
        elif (play_again == "N") or (play_again == "n"):
            return True
        else:
            play_again = input("Play again (Y/N)? ")


def run_guessing_game(words_filepath):
    """Controls running The Guessing Game. This includes parsing
    the words file and executing multiple rounds of the game.

    :param words_filepath: the location of the file of words for the game
    :return: None
    """
    try:
        lst_words = read_words(words_filepath)
    except FileNotFoundError:
        print("The provided file location is not valid. Please enter a valid path to a file.")
        return

    print("Welcome to The Guessing Game!")

    status_complete_game = False

    while not status_complete_game:
        # try:
        #     lst_words = read_words(words_filepath)
        # except FileNotFoundError:
        #     print("The provided file location is not valid. Please enter a valid path to a file.")
        #     return

        rand_word = get_word(lst_words)
        rand_word_lst = list(rand_word)
        blank_word_lst = blank_chars(rand_word)
        misses = []
        status_round = is_round_complete(blank_word_lst, misses)

        while not status_round:  # while round is not complete
            display_game_state(blank_word_lst, misses)
            user_guess = get_guess()
            guess_position = check_guess(rand_word, user_guess)
            update_state(blank_word_lst, misses, user_guess, guess_position)

            if is_round_complete(blank_word_lst, misses):
                display_game_state(rand_word_lst, misses)

                if not is_game_complete():
                    status_complete_game = False
                    try:
                        lst_words = read_words(words_filepath)
                    except FileNotFoundError:
                        print("The provided file location is not valid. Please enter a valid path to a file.")
                        return
                    rand_word = get_word(lst_words)
                    rand_word_lst = list(rand_word)
                    blank_word_lst = blank_chars(rand_word)
                    misses = []

                else:
                    status_complete_game = True
                    print("\nGoodbye.")
                    break


def main():
    ########## DO NOT EDIT ASSIGNMENT STATEMENT BELOW #########

    filepath = sys.argv[-1]

    ########## DO NOT EDIT ASSIGNMENT STATEMENT ABOVE #########

    # call run_guessing_game() with filepath as argument and remove pass below
    run_guessing_game("word_file.txt")


if __name__ == '__main__':
    main()
