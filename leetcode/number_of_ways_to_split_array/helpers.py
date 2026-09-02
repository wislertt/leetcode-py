def run_ways_to_split_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.ways_to_split_array(nums)


def assert_ways_to_split_array(result: int, expected: int) -> bool:
    assert result == expected
    return True
