def run_time_taken(solution_class: type, arrival: list[int], state: list[int]):
    implementation = solution_class()
    return implementation.time_taken(arrival, state)


def assert_time_taken(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
