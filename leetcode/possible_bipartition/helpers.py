def run_possible_bipartition(solution_class: type, n: int, dislikes: list[list[int]]):
    implementation = solution_class()
    return implementation.possible_bipartition(n, dislikes)


def assert_possible_bipartition(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
