def run_dominant_index(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.dominant_index(nums)


def assert_dominant_index(result: int, expected: int) -> bool:
    assert result == expected
    return True
