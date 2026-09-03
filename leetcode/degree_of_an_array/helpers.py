def run_find_shortest_sub_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_shortest_sub_array(nums)


def assert_find_shortest_sub_array(result: int, expected: int) -> bool:
    assert result == expected
    return True
