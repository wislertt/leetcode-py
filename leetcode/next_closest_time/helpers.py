def run_next_closest_time(solution_class: type, time: str):
    implementation = solution_class()
    return implementation.next_closest_time(time)


def assert_next_closest_time(result: str, expected: str) -> bool:
    assert result == expected
    return True
