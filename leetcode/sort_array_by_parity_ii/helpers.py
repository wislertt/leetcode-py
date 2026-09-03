def run_sort_array_by_parity_ii(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.sort_array_by_parity_ii(nums)


def assert_sort_array_by_parity_ii(result: list[int], expected: list[int]) -> bool:
    # Any arrangement with the same multiset and parity matching each index is valid
    assert sorted(result) == sorted(expected)
    assert all(value % 2 == index % 2 for index, value in enumerate(result))
    return True
