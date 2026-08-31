def run_minimum_total(solution_class: type, triangle: list[list[int]]):
    implementation = solution_class()
    return implementation.minimum_total(triangle)


def assert_minimum_total(result: int, expected: int) -> bool:
    assert result == expected
    return True
