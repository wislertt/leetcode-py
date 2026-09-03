def run_count_triplets(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.count_triplets(nums)


def assert_count_triplets(result: int, expected: int) -> bool:
    assert result == expected
    return True
