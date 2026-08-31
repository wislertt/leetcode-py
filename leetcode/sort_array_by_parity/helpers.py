def run_sort_array_by_parity(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.sort_array_by_parity(nums)


def assert_sort_array_by_parity(result: list[int], expected: list[int]) -> bool:
    # Any arrangement with the same multiset, evens first then odds, is valid
    assert sorted(result) == sorted(expected)
    odd_seen = False
    for value in result:
        if value % 2 == 1:
            odd_seen = True
        else:
            assert not odd_seen
    return True
