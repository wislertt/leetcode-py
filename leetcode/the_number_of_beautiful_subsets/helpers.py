def run_beautiful_subsets(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.beautiful_subsets(nums, k)


def assert_beautiful_subsets(result: int, expected: int) -> bool:
    assert result == expected
    return True
