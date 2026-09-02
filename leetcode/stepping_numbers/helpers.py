def run_count_stepping_numbers(solution_class: type, low: int, high: int):
    implementation = solution_class()
    return implementation.count_stepping_numbers(low, high)


def assert_count_stepping_numbers(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
