def run_get_money_amount(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.get_money_amount(n)


def assert_get_money_amount(result: int, expected: int) -> bool:
    assert result == expected
    return True
