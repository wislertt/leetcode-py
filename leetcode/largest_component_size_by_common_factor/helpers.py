def run_largest_component_size(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.largest_component_size(nums)


def assert_largest_component_size(result: int, expected: int) -> bool:
    assert result == expected
    return True
