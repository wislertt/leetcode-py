def assert_solve_n_queens_solution_count(result: list[list[str]], expected: int) -> bool:
    assert len(result) == expected
    return True


def run_solve_n_queens(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.solve_n_queens(n)


def assert_solve_n_queens(result: list[list[str]], expected: list[list[str]]) -> bool:
    # Sort both result and expected for order-independent comparison
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
