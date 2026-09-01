def run_distribute_candies(solution_class: type, n: int, limit: int):
    implementation = solution_class()
    return implementation.distribute_candies(n, limit)


def assert_distribute_candies(result: int, expected: int) -> bool:
    assert result == expected
    return True
