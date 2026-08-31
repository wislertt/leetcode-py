def run_cheapest_jump(solution_class: type, coins: list[int], max_jump: int):
    implementation = solution_class()
    return implementation.cheapest_jump(coins, max_jump)


def assert_cheapest_jump(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
