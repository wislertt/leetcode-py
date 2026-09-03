def run_triangle_number(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.triangle_number(nums)


def assert_triangle_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
