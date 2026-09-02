def run_largest_odd_number(solution_class: type, num: str):
    implementation = solution_class()
    return implementation.largest_odd_number(num)


def assert_largest_odd_number(result: str, expected: str) -> bool:
    assert result == expected
    return True
