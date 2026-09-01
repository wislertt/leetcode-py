def run_max_value_of_coins(solution_class: type, piles: list[list[int]], k: int):
    implementation = solution_class()
    return implementation.max_value_of_coins(piles, k)


def assert_max_value_of_coins(result: int, expected: int) -> bool:
    assert result == expected
    return True
