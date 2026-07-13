def run_min_sub_array_len(solution_class: type, target: int, nums: list[int]):
    implementation = solution_class()
    return implementation.min_sub_array_len(target, nums)


def assert_min_sub_array_len(result: int, expected: int) -> bool:
    assert result == expected
    return True
