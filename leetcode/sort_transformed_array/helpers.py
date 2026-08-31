def run_sort_transformed_array(solution_class: type, nums: list[int], a: int, b: int, c: int):
    implementation = solution_class()
    return implementation.sort_transformed_array(nums, a, b, c)


def assert_sort_transformed_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
