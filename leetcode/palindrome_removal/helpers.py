def run_minimum_moves(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.minimum_moves(arr)


def assert_minimum_moves(result: int, expected: int) -> bool:
    assert result == expected
    return True
