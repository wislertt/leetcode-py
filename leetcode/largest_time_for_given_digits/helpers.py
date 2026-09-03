def run_largest_time_from_digits(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.largest_time_from_digits(arr)


def assert_largest_time_from_digits(result: str, expected: str) -> bool:
    assert result == expected
    return True
