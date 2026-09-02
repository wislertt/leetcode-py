def run_min_score(solution_class: type, n: int, roads: list[list[int]]):
    implementation = solution_class()
    return implementation.min_score(n, roads)


def assert_min_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
