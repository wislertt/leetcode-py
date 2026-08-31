def run_number_of_substrings(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.number_of_substrings(s)


def assert_number_of_substrings(result: int, expected: int) -> bool:
    assert result == expected
    return True
