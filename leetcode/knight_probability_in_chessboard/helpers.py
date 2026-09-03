import math


def run_knight_probability(solution_class: type, n: int, k: int, row: int, column: int):
    implementation = solution_class()
    return implementation.knight_probability(n, k, row, column)


def assert_knight_probability(result: float, expected: float) -> bool:
    # LeetCode accepts answers within 1e-6 of the reference
    assert math.isclose(result, expected, rel_tol=0.0, abs_tol=1e-6)
    return True
