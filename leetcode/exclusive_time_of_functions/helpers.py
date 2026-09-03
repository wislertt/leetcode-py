def run_exclusive_time(solution_class: type, n: int, logs: list[str]):
    implementation = solution_class()
    return implementation.exclusive_time(n, logs)


def assert_exclusive_time(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
