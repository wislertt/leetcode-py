def run_is_ideal_permutation(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.is_ideal_permutation(nums)


def assert_is_ideal_permutation(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
