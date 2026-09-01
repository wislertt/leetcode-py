def run_maximum_importance(solution_class: type, n: int, roads: list[list[int]]):
    implementation = solution_class()
    return implementation.maximum_importance(n, roads)


def assert_maximum_importance(result: int, expected: int) -> bool:
    assert result == expected
    return True
