"""COMP 110 exercise 2 - creating wordle in python"""

__author__: str = "730552953"


def contains_char(word: str, search: str) -> bool:
    """Searches through words for characters"""
    assert len(search) == 1, f"len('{search}') is not 1"
    search_index: int = 0
    while search_index < len(word):
        if search != word[search_index]:
            search_index = search_index + 1
        else:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret), "Guess must be same length as secret"
    search_index: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    while search_index < len(guess):
        if guess[search_index] == secret[search_index]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[search_index]) == True:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        search_index = search_index + 1
    return result


def input_guess(expected_length: int) -> str:
    word_entry = input(f"Enter a {expected_length} character word")
    while len(word_entry) != expected_length:
        print(f"That wasn't {expected_length} chars! Try again:")
        word_entry = input(f"Enter a {expected_length} character word")
    return word_entry


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        wordle_guess = input_guess(len(secret))
        print(emojified(wordle_guess, secret))
        if wordle_guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn = turn + 1
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main(secret="codes")
