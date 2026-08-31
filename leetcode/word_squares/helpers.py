def assert_word_squares_solution_count(result: list[list[str]], expected: int) -> bool:
    assert len(result) == expected
    return True


def run_word_squares(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.word_squares(words)


def assert_word_squares(result: list[list[str]], expected: list[list[str]]) -> bool:
    # Sort both result and expected for order-independent comparison
    assert sorted(result) == sorted(expected)
    return True
