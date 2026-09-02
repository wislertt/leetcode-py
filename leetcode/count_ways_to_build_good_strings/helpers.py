def run_count_good_strings(solution_class: type, low: int, high: int, zero: int, one: int):
    implementation = solution_class()
    return implementation.count_good_strings(low, high, zero, one)


def assert_count_good_strings(result: int, expected: int) -> bool:
    assert result == expected
    return True
