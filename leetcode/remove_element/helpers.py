def run_remove_element(solution_class: type, nums: list[int], val: int):
    implementation = solution_class()
    k = implementation.remove_element(nums, val)
    return k, sorted(nums[:k])


def assert_remove_element(result: tuple[int, list[int]], expected: tuple[int, list[int]]) -> bool:
    assert result == expected
    return True
