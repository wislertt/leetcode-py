def run_count_paths(solution_class: type, n: int, roads: list[list[int]]):
    implementation = solution_class()
    return implementation.count_paths(n, roads)


def assert_count_paths(result: int, expected: int) -> bool:
    assert result == expected
    return True
