def run_total_money(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.total_money(n)


def assert_total_money(result: int, expected: int) -> bool:
    assert result == expected
    return True
