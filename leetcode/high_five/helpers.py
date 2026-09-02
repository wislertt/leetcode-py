def run_high_five(solution_class: type, items: list[list[int]]):
    implementation = solution_class()
    return implementation.high_five(items)


def assert_high_five(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
