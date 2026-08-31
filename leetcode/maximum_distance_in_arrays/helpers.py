def run_max_distance(solution_class: type, arrays: list[list[int]]):
    implementation = solution_class()
    return implementation.max_distance(arrays)


def assert_max_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
