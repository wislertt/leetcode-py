def run_is_armstrong(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.is_armstrong(n)


def assert_is_armstrong(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
