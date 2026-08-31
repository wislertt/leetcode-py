def run_largest_divisible_subset(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.largest_divisible_subset(nums)


def assert_largest_divisible_subset(result: list[int], expected: list[int]) -> bool:
    # Multiple valid answers exist; verify the result is a valid
    # divisible chain of the maximum length rather than exact equality
    assert len(result) == len(expected)
    chain = sorted(result)
    assert all(chain[i + 1] % chain[i] == 0 for i in range(len(chain) - 1))
    return True
