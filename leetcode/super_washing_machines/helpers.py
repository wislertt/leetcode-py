def run_find_min_moves(solution_class: type, machines: list[int]):
    implementation = solution_class()
    return implementation.find_min_moves(machines)


def assert_find_min_moves(result: int, expected: int) -> bool:
    assert result == expected
    return True
