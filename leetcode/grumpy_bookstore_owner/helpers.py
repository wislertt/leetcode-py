def run_max_satisfied(solution_class: type, customers: list[int], grumpy: list[int], minutes: int):
    implementation = solution_class()
    return implementation.max_satisfied(customers, grumpy, minutes)


def assert_max_satisfied(result: int, expected: int) -> bool:
    assert result == expected
    return True
