def run_length_of_last_word(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.length_of_last_word(s)


def assert_length_of_last_word(result: int, expected: int) -> bool:
    assert result == expected
    return True
