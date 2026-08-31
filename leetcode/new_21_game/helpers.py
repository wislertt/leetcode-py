def run_new21_game(solution_class: type, n: int, k: int, max_pts: int):
    implementation = solution_class()
    return implementation.new21_game(n, k, max_pts)


def assert_new21_game(result: float, expected: float) -> bool:
    # The statement accepts answers within 10^-5 of the actual answer
    assert abs(result - expected) < 1e-5
    return True
