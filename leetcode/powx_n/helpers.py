def run_my_pow(solution_class: type, x: float, n: int):
    implementation = solution_class()
    return implementation.my_pow(x, n)


def assert_my_pow(result: float, expected: float) -> bool:
    assert abs(result - expected) < 1e-5, f"Expected {expected}, got {result}"
    return True
