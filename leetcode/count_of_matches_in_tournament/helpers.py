def run_number_of_matches(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.number_of_matches(n)


def assert_number_of_matches(result: int, expected: int) -> bool:
    assert result == expected
    return True
