def run_merge_stones(solution_class: type, stones: list[int], k: int):
    implementation = solution_class()
    return implementation.merge_stones(stones, k)


def assert_merge_stones(result: int, expected: int) -> bool:
    assert result == expected
    return True
