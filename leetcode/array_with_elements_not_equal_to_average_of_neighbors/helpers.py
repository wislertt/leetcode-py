def run_rearrange_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.rearrange_array(nums)


def assert_rearrange_array(result: list[int], expected: list[int]) -> bool:
    # Multiple valid answers exist; verify the non-average property and that the
    # result is a permutation of the input instead of exact equality
    assert all(2 * result[i] != result[i - 1] + result[i + 1] for i in range(1, len(result) - 1))
    assert sorted(result) == sorted(expected)
    return True
