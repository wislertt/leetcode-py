def run_distribute_candies(solution_class: type, candy_type: list[int]):
    implementation = solution_class()
    return implementation.distribute_candies(candy_type)


def assert_distribute_candies(result: int, expected: int) -> bool:
    assert result == expected
    return True
