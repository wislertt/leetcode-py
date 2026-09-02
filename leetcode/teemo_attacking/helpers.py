def run_find_poisoned_duration(solution_class: type, time_series: list[int], duration: int):
    implementation = solution_class()
    return implementation.find_poisoned_duration(time_series, duration)


def assert_find_poisoned_duration(result: int, expected: int) -> bool:
    assert result == expected
    return True
