from hangman_folder.game import is_won, is_lost


def prompt_guess() -> str:
    user_guess = input("Please enter a letter \n")
    return user_guess

def print_status(state: dict) -> None:
    print(f"{" ".join(state["display"])}  \nYour guessed letters are {state["guessed"]}"
          f"\nyour have {state["max_tries"] - state["wrong_guesses"]} attempts remaining")

def print_result(state: dict) -> None:
    if is_won(state):
        print("You have won!")
    if is_lost(state):
        print("you have lost!")
    print(f"The word was {state["secret"]}")

