def run_max_kelements(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.max_kelements(nums, k)


def assert_max_kelements(result: int, expected: int) -> bool:
    assert result == expected
    return True
