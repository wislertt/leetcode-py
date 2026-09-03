def run_at_most_n_given_digit_set(solution_class: type, digits: list[str], n: int):
    implementation = solution_class()
    return implementation.at_most_n_given_digit_set(digits, n)


def assert_at_most_n_given_digit_set(result: int, expected: int) -> bool:
    assert result == expected
    return True
