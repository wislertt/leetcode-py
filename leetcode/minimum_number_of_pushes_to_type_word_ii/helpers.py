def run_minimum_pushes(solution_class: type, word: str):
    implementation = solution_class()
    return implementation.minimum_pushes(word)


def assert_minimum_pushes(result: int, expected: int) -> bool:
    assert result == expected
    return True
