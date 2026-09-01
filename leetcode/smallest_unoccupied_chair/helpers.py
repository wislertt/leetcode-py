def run_smallest_chair(solution_class: type, times: list[list[int]], target_friend: int):
    implementation = solution_class()
    return implementation.smallest_chair(times, target_friend)


def assert_smallest_chair(result: int, expected: int) -> bool:
    assert result == expected
    return True
