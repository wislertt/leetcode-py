def run_num_jewels_in_stones(solution_class: type, jewels: str, stones: str):
    implementation = solution_class()
    return implementation.num_jewels_in_stones(jewels, stones)


def assert_num_jewels_in_stones(result: int, expected: int) -> bool:
    assert result == expected
    return True
