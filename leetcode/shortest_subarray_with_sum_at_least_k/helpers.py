def run_shortest_subarray(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.shortest_subarray(nums, k)


def assert_shortest_subarray(result: int, expected: int) -> bool:
    assert result == expected
    return True
