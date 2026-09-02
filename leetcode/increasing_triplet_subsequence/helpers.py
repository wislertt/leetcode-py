def run_increasing_triplet(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.increasing_triplet(nums)


def assert_increasing_triplet(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
