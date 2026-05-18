def run_multiply(solution_class: type, num1: str, num2: str):
    implementation = solution_class()
    return implementation.multiply(num1, num2)


def assert_multiply(result: str, expected: str) -> bool:
    assert result == expected
    return True
