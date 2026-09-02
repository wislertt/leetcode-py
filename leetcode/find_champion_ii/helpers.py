def run_find_champion(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.find_champion(n, edges)


def assert_find_champion(result: int, expected: int) -> bool:
    assert result == expected
    return True
