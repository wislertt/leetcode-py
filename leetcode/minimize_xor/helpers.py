def run_minimize_xor(solution_class: type, num1: int, num2: int):
    implementation = solution_class()
    return implementation.minimize_xor(num1, num2)


def assert_minimize_xor(result: int, expected: int) -> bool:
    assert result == expected
    return True
