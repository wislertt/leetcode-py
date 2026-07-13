def run_last_stone_weight_ii(solution_class: type, stones: list[int]):
    implementation = solution_class()
    return implementation.last_stone_weight_ii(stones)


def assert_last_stone_weight_ii(result: int, expected: int) -> bool:
    assert result == expected
    return True
