def run_xor_game(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.xor_game(nums)


def assert_xor_game(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
