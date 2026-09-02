def run_maximum_score(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.maximum_score(nums, k)


def assert_maximum_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
