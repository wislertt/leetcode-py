def run_shifting_letters(solution_class: type, s: str, shifts: list[list[int]]):
    implementation = solution_class()
    return implementation.shifting_letters(s, shifts)


def assert_shifting_letters(result: str, expected: str) -> bool:
    assert result == expected
    return True
