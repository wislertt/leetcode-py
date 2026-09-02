def run_min_cost(solution_class: type, colors: str, needed_time: list[int]):
    implementation = solution_class()
    return implementation.min_cost(colors, needed_time)


def assert_min_cost(result: int, expected: int) -> bool:
    assert result == expected
    return True
