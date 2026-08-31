def run_number_of_patterns(solution_class: type, m: int, n: int):
    implementation = solution_class()
    return implementation.number_of_patterns(m, n)


def assert_number_of_patterns(result: int, expected: int) -> bool:
    assert result == expected
    return True
