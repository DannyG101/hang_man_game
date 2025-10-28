from hangman_folder.game import init_state, validate_guess, apply_guess, is_won, is_lost
from hangman_folder.io import prompt_guess, print_status, print_result
from hangman_folder.words import choose_secret_word
from data.word_collection import words_collection


def play(words: list[str], max_tries: int = 20) -> None:
    secret_word = choose_secret_word(words)
    game_state = init_state(secret_word, max_tries)
    print("Welcome to this hangman game")
    print(" ".join(game_state["display"]))
    while not is_won(game_state) and not is_lost(game_state):
        user_guess = prompt_guess()
        valid_guess = validate_guess(user_guess, game_state["guessed"])
        if valid_guess[0]:
            round_results = apply_guess(game_state, user_guess)
            if round_results:
                print("WELL DONE THATS CORRECT")
                print_status(game_state)
            else:
                print("SORRY THATS INCORRECT")
                print_status(game_state)
        else:
            print("Wrong input")

    print_result(game_state)





if __name__ == "__main__":
    play(words_collection)
