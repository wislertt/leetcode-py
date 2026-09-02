def run_sequential_digits(solution_class: type, low: int, high: int):
    implementation = solution_class()
    return implementation.sequential_digits(low, high)


def assert_sequential_digits(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
