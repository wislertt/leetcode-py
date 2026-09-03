def run_partition_disjoint(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.partition_disjoint(nums)


def assert_partition_disjoint(result: int, expected: int) -> bool:
    assert result == expected
    return True
