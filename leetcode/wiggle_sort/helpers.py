def run_wiggle_sort(solution_class: type, nums: list[int]):
    implementation = solution_class()
    nums_copy = nums.copy()
    implementation.wiggle_sort(nums_copy)
    return nums_copy


def assert_wiggle_sort(result: list[int], expected: list[int]) -> bool:
    # Multiple valid answers exist; verify the wiggle property and that
    # the result is a permutation of the input instead of exact equality
    assert all(
        (result[i] >= result[i - 1] if i % 2 == 1 else result[i] <= result[i - 1])
        for i in range(1, len(result))
    )
    assert sorted(result) == sorted(expected)
    return True
