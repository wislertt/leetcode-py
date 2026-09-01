def run_maximum_beauty(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.maximum_beauty(nums, k)


def assert_maximum_beauty(result: int, expected: int) -> bool:
    assert result == expected
    return True
