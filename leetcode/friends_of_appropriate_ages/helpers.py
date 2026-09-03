def run_num_friend_requests(solution_class: type, ages: list[int]):
    implementation = solution_class()
    return implementation.num_friend_requests(ages)


def assert_num_friend_requests(result: int, expected: int) -> bool:
    assert result == expected
    return True
