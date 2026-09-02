def run_min_transfers(solution_class: type, transactions: list[list[int]]):
    implementation = solution_class()
    return implementation.min_transfers(transactions)


def assert_min_transfers(result: int, expected: int) -> bool:
    assert result == expected
    return True
