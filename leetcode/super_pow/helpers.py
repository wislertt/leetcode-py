def run_super_pow(solution_class: type, a: int, b: list[int]):
    implementation = solution_class()
    return implementation.super_pow(a, b)


def assert_super_pow(result: int, expected: int) -> bool:
    assert result == expected, f"Expected {expected}, got {result}"
    return True
