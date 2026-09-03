from .solution import Master


def run_find_secret_word(solution_class: type, secret: str, words: list[str], allowed_guesses: int):
    master = Master(secret, words, allowed_guesses)
    solution_class().find_secret_word(words, master)
    return master.outcome()


def assert_find_secret_word(result: bool, expected: bool) -> bool:
    assert result is expected
    return True
