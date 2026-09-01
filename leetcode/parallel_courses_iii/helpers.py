def run_minimum_time(solution_class: type, n: int, relations: list[list[int]], time: list[int]):
    implementation = solution_class()
    return implementation.minimum_time(n, relations, time)


def assert_minimum_time(result: int, expected: int) -> bool:
    assert result == expected
    return True
