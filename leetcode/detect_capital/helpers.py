def run_detect_capital_use(solution_class: type, word: str):
    implementation = solution_class()
    return implementation.detect_capital_use(word)


def assert_detect_capital_use(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
