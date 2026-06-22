def run_last_stone_weight(solution_class: type, stones: list[int]):
    implementation = solution_class()
    return implementation.last_stone_weight(stones)


def assert_last_stone_weight(result: int, expected: int) -> bool:
    assert result == expected
    return True
