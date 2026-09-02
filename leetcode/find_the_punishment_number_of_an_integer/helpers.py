def run_punishment_number(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.punishment_number(n)


def assert_punishment_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
