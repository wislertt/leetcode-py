def run_longest_mountain(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.longest_mountain(arr)


def assert_longest_mountain(result: int, expected: int) -> bool:
    assert result == expected
    return True
