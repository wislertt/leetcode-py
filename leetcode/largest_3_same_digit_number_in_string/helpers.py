def run_largest_good_integer(solution_class: type, num: str):
    implementation = solution_class()
    return implementation.largest_good_integer(num)


def assert_largest_good_integer(result: str, expected: str) -> bool:
    assert result == expected
    return True
