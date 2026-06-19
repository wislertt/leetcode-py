def run_solve(solution_class: type, board: list[list[str]]):
    implementation = solution_class()
    work = [list(row) for row in board]
    implementation.solve(work)
    return work


def assert_solve(result: list[list[str]], expected: list[list[str]]) -> bool:
    assert result == expected
    return True
