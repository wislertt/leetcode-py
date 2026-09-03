def run_valid_mountain_array(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.valid_mountain_array(arr)


def assert_valid_mountain_array(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
