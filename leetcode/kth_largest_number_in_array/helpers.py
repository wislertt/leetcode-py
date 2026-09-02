def run_kth_largest_number(solution_class: type, nums: list[str], k: int):
    implementation = solution_class()
    return implementation.kth_largest_number(nums, k)


def assert_kth_largest_number(result: str, expected: str) -> bool:
    assert result == expected
    return True
