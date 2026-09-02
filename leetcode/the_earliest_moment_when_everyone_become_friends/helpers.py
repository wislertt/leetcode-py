def run_earliest_acq(solution_class: type, logs: list[list[int]], n: int):
    implementation = solution_class()
    return implementation.earliest_acq(logs, n)


def assert_earliest_acq(result: int, expected: int) -> bool:
    assert result == expected
    return True
