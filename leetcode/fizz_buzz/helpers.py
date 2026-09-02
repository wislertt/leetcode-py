def run_fizz_buzz(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.fizz_buzz(n)


def assert_fizz_buzz(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
