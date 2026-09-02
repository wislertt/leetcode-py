def run_min_patches(solution_class: type, nums: list[int], n: int):
    implementation = solution_class()
    return implementation.min_patches(nums, n)


def assert_min_patches(result: int, expected: int) -> bool:
    assert result == expected
    return True
