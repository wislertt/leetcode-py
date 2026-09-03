def run_order_of_largest_plus_sign(solution_class: type, n: int, mines: list[list[int]]):
    implementation = solution_class()
    return implementation.order_of_largest_plus_sign(n, mines)


def assert_order_of_largest_plus_sign(result: int, expected: int) -> bool:
    assert result == expected
    return True
