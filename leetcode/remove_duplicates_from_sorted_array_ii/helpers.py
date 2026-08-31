def run_remove_duplicates(solution_class: type, nums: list[int]):
    implementation = solution_class()
    k = implementation.remove_duplicates(nums)
    return k, nums[:k]


def assert_remove_duplicates(
    result: tuple[int, list[int]], expected: tuple[int, list[int]]
) -> bool:
    assert result == expected
    return True
