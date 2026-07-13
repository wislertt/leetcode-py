def run_split_array(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.split_array(nums, k)


def assert_split_array(result: int, expected: int) -> bool:
    assert result == expected
    return True
