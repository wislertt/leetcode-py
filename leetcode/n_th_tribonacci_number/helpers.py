def run_tribonacci(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.tribonacci(n)


def assert_tribonacci(result: int, expected: int) -> bool:
    assert result == expected
    return True
