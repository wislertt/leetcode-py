def run_largest_perimeter(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.largest_perimeter(nums)


def assert_largest_perimeter(result: int, expected: int) -> bool:
    assert result == expected
    return True
