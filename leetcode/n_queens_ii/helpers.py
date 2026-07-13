def run_total_n_queens(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.total_n_queens(n)


def assert_total_n_queens(result: int, expected: int) -> bool:
    assert result == expected
    return True
