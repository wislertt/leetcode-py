def run_shuffle(solution_class: type, nums: list[int], n: int):
    implementation = solution_class()
    return implementation.shuffle(nums, n)


def assert_shuffle(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
