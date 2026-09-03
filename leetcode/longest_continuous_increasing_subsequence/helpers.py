def run_find_length_of_lcis(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_length_of_lcis(nums)


def assert_find_length_of_lcis(result: int, expected: int) -> bool:
    assert result == expected
    return True
