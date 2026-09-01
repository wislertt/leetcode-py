def run_find_unique_binary_string(solution_class: type, nums: list[str]):
    implementation = solution_class()
    return implementation.find_unique_binary_string(nums)


def assert_find_unique_binary_string(result: str, expected: str) -> bool:
    # Multiple valid answers exist; verify shape and binary alphabet here.
    # Uniqueness against nums is asserted in the test body, which has nums.
    assert len(result) == len(expected)
    assert set(result) <= {"0", "1"}
    return True
