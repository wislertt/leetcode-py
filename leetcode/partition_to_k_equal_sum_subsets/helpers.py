def run_can_partition_k_subsets(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.can_partition_k_subsets(nums, k)


def assert_can_partition_k_subsets(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
