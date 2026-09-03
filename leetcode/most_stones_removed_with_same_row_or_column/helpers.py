def run_remove_stones(solution_class: type, stones: list[list[int]]):
    implementation = solution_class()
    return implementation.remove_stones(stones)


def assert_remove_stones(result: int, expected: int) -> bool:
    assert result == expected
    return True
