

def init_state(secret: str, max_tries: int) -> dict:
    return {"secret":secret, "display": display(secret), "guessed":set(), "wrong_guesses":0, "max_tries": max_tries}

def display(word):
    display_word = []
    for i in range(len(word)):
            display_word.append("_")
    return display_word

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if ch.isalpha() and ch not in guessed and len(ch) == 1:
        return True, "valid attempt"
    return False, "not a valid attempt"

def apply_guess(state: dict, ch: str) -> bool:
    is_successful = False
    for i in range(len(state["secret"])):
        if ch == state["secret"][i]:
            state["display"][i] = ch
            is_successful = True

    if not is_successful:
        state["wrong_guesses"] += 1

    state["guessed"].add(ch)
    return is_successful






def is_won(state: dict) -> bool:
    if "".join(state["display"]) == state["secret"]:
        return True
    return False

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    return False

def render_display(state: dict) -> str:
    return state["display"]

def render_summary(state: dict) -> str:
    return f"The word is {state["secret"]}, your guesses were {state["guessed"]}"
