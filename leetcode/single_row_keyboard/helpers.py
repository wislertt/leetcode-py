def run_calculate_time(solution_class: type, keyboard: str, word: str):
    implementation = solution_class()
    return implementation.calculate_time(keyboard, word)


def assert_calculate_time(result: int, expected: int) -> bool:
    assert result == expected
    return True
