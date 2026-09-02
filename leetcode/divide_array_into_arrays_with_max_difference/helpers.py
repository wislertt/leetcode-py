def run_divide_array(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.divide_array(nums, k)


def assert_divide_array(result: list[list[int]], expected: list[list[int]], k: int) -> bool:
    # Multiple valid divisions exist; verify the result is a valid
    # partition of the same multiset with every group within k
    if not expected:
        assert result == []
        return True
    assert len(result) == len(expected)
    assert all(len(group) == 3 for group in result)
    assert sorted(x for group in result for x in group) == sorted(
        x for group in expected for x in group
    )
    assert all(max(group) - min(group) <= k for group in result)
    return True
