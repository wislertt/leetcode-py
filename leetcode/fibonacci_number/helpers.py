def run_fib(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.fib(n)


def assert_fib(result: int, expected: int) -> bool:
    assert result == expected
    return True
