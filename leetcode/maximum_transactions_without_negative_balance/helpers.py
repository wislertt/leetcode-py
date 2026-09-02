def run_max_transactions(solution_class: type, transactions: list[int]):
    implementation = solution_class()
    return implementation.max_transactions(transactions)


def assert_max_transactions(result: int, expected: int) -> bool:
    assert result == expected
    return True
