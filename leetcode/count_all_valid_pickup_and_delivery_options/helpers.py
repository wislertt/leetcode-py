def run_count_orders(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_orders(n)


def assert_count_orders(result: int, expected: int) -> bool:
    assert result == expected
    return True
