from collections import Counter


def run_find_matrix(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_matrix(nums)


def assert_find_matrix(result: list[list[int]], expected: list[int]) -> bool:
    # Multiple valid answers exist; expected is sorted(nums). Verify every
    # element is used exactly once, each row is distinct, and the row count
    # is minimal (equal to the maximum frequency)
    assert sorted(x for row in result for x in row) == expected
    assert all(len(row) == len(set(row)) for row in result)
    assert len(result) == max(Counter(expected).values())
    return True
