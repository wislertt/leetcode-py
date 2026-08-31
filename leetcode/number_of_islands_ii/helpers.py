def run_num_islands2(solution_class: type, m: int, n: int, positions: list[list[int]]):
    implementation = solution_class()
    return implementation.num_islands2(m, n, positions)


def assert_num_islands2(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
