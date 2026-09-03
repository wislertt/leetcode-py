def run_num_squareful_perms(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.num_squareful_perms(nums)


def assert_num_squareful_perms(result: int, expected: int) -> bool:
    assert result == expected
    return True
