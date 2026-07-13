def run_open_lock(solution_class: type, deadends: list[str], target: str):
    implementation = solution_class()
    return implementation.open_lock(deadends, target)


def assert_open_lock(result: int, expected: int) -> bool:
    assert result == expected
    return True
