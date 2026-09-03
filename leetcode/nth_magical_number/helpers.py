def run_nth_magical_number(solution_class: type, n: int, a: int, b: int):
    implementation = solution_class()
    return implementation.nth_magical_number(n, a, b)


def assert_nth_magical_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
