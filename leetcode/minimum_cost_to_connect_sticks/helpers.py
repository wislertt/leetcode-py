def run_connect_sticks(solution_class: type, sticks: list[int]):
    implementation = solution_class()
    return implementation.connect_sticks(sticks)


def assert_connect_sticks(result: int, expected: int) -> bool:
    assert result == expected
    return True
